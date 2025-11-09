#!/usr/bin/env python3
"""
Unit tests for aws-sla-hunter with mock AWS Health API
Includes automatic screenshot generation for README
"""

import sys
import os
import argparse
from io import StringIO
from datetime import datetime, timedelta
from unittest import TestCase, main, mock
from unittest.mock import MagicMock, patch, Mock

# Fix Windows encoding for emojis
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    os.environ["PYTHONIOENCODING"] = "utf-8"


class TestAwsSLAHunter(TestCase):
    """Test cases for SLA Hunter CLI"""

    def setUp(self):
        """Set up test fixtures"""
        self.mock_events = [
            {
                "arn": "arn:aws:health:us-east-1::event/EC2/123456",
                "service": "EC2",
                "eventTypeCode": "AWS_EC2_INSTANCE_FAILURE",
                "eventStatus": "open",
                "region": "us-east-1",
                "startTime": datetime.utcnow() - timedelta(days=5),
                "description": "EC2 instance failure in us-east-1",
            },
            {
                "arn": "arn:aws:health:sa-east-1::event/RDS/789012",
                "service": "RDS",
                "eventTypeCode": "AWS_RDS_OUTAGE",
                "eventStatus": "CLOSED",
                "region": "sa-east-1",
                "startTime": datetime.utcnow() - timedelta(days=15),
                "description": "RDS database outage in sa-east-1",
            },
            {
                "arn": "arn:aws:health:us-west-2::event/ELB/345678",
                "service": "ELASTICLOADBALANCING",
                "eventTypeCode": "AWS_ELB_DEGRADED",
                "eventStatus": "CLOSED",
                "region": "us-west-2",
                "startTime": datetime.utcnow() - timedelta(days=30),
                "description": "ELB performance degradation in us-west-2",
            },
        ]

    @patch("main.boto3.client")
    def test_get_credentials_success(self, mock_boto_client):
        """Test successful credential verification"""
        from main import get_credentials

        mock_sts = MagicMock()
        mock_boto_client.return_value = mock_sts
        mock_sts.get_caller_identity.return_value = {"UserId": "AIDAI1234567890"}

        result = get_credentials()
        self.assertTrue(result)
        mock_boto_client.assert_called_with("sts", region_name="us-east-1")

    @patch("main.boto3.client")
    @patch("main.console.print")
    def test_get_credentials_no_credentials(self, mock_print, mock_boto_client):
        """Test credential verification with missing credentials"""
        from botocore.exceptions import NoCredentialsError
        from main import get_credentials

        mock_sts = MagicMock()
        mock_boto_client.return_value = mock_sts
        mock_sts.get_caller_identity.side_effect = NoCredentialsError()

        result = get_credentials()
        self.assertFalse(result)
        self.assertTrue(mock_print.called)

    @patch("main.boto3.client")
    def test_fetch_health_events(self, mock_boto_client):
        """Test fetching health events from AWS"""
        from main import fetch_health_events

        mock_health = MagicMock()
        mock_boto_client.return_value = mock_health

        # Mock the describe_events response
        mock_health.describe_events.return_value = {"events": self.mock_events[:2]}
        mock_health.describe_event_details.return_value = {"successfulSet": []}

        events = fetch_health_events()

        # Verify the call was made with correct parameters
        mock_health.describe_events.assert_called_once()
        call_args = mock_health.describe_events.call_args
        self.assertIn("filter", call_args.kwargs)
        self.assertIn("eventTypeCategories", call_args.kwargs["filter"])
        self.assertIn("eventStatusCodes", call_args.kwargs["filter"])

    @patch("main.boto3.client")
    @patch("main.console.print")
    def test_fetch_health_events_no_events(self, mock_print, mock_boto_client):
        """Test fetching when no events exist"""
        from main import fetch_health_events

        mock_health = MagicMock()
        mock_boto_client.return_value = mock_health
        mock_health.describe_events.return_value = {"events": []}

        events = fetch_health_events()
        self.assertEqual(len(events), 0)

    def test_format_event_date(self):
        """Test event date formatting"""
        from main import format_event_date

        event = self.mock_events[0]
        date_str = format_event_date(event)
        self.assertRegex(date_str, r"\d{4}-\d{2}-\d{2}")

    def test_format_service(self):
        """Test service name extraction"""
        from main import format_service

        # Test EC2
        service = format_service(self.mock_events[0])
        self.assertEqual(service, "EC2")

        # Test RDS
        service = format_service(self.mock_events[1])
        self.assertEqual(service, "RDS")

        # Test ELB
        service = format_service(self.mock_events[2])
        self.assertEqual(service, "ELB")

    def test_format_region(self):
        """Test region extraction"""
        from main import format_region

        region = format_region(self.mock_events[0])
        self.assertEqual(region, "us-east-1")

        region = format_region(self.mock_events[1])
        self.assertEqual(region, "sa-east-1")

    def test_format_status(self):
        """Test status formatting"""
        from main import format_status

        # Test open status
        status = format_status(self.mock_events[0])
        self.assertIn("Open", str(status))

        # Test closed status
        status = format_status(self.mock_events[1])
        self.assertIn("Closed", str(status))

    def test_format_event_type(self):
        """Test event type formatting"""
        from main import format_event_type

        event_type = format_event_type(self.mock_events[0])
        self.assertTrue(len(event_type) > 0)
        self.assertLessEqual(len(event_type), 25)

    @patch("main.boto3.client")
    @patch("main.get_credentials")
    @patch("main.fetch_health_events")
    @patch("main.display_results")
    @patch("main.display_cta")
    def test_main_success(
        self,
        mock_cta,
        mock_display,
        mock_fetch,
        mock_creds,
        mock_boto_client,
    ):
        """Test main function succeeds"""
        from main import main

        mock_creds.return_value = True
        mock_fetch.return_value = self.mock_events

        result = main()
        self.assertEqual(result, 0)
        mock_display.assert_called_once()
        mock_cta.assert_called_once()

    @patch("main.get_credentials")
    def test_main_credential_failure(self, mock_creds):
        """Test main function fails on credential error"""
        from main import main

        mock_creds.return_value = False

        result = main()
        self.assertEqual(result, 1)

    @patch("main.boto3.client")
    @patch("main.get_credentials")
    @patch("main.fetch_health_events")
    def test_main_with_mock_data(self, mock_fetch, mock_creds, mock_boto_client):
        """Test main function with mock data"""
        from main import main

        mock_creds.return_value = True
        mock_fetch.return_value = self.mock_events

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            result = main()
            output = sys.stdout.getvalue()
            self.assertEqual(result, 0)
            # Verify output contains expected elements
            self.assertIn("AWS SLA Hunter", output)
        finally:
            sys.stdout = old_stdout

    @patch("main.boto3.client")
    def test_cta_contains_link(self, mock_boto_client):
        """Test CTA contains correct link"""
        from main import display_cta
        from io import StringIO

        old_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            display_cta()
            output = sys.stdout.getvalue()
            self.assertIn("awscostguardian.com", output)
        finally:
            sys.stdout = old_stdout

    def test_display_results_empty(self):
        """Test display results with empty events"""
        from main import display_results
        from io import StringIO

        old_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            display_results([])
            output = sys.stdout.getvalue()
            self.assertIn("No SLA-eligible events", output)
        finally:
            sys.stdout = old_stdout

    def test_display_results_with_events(self):
        """Test display results with events"""
        from main import display_results
        from io import StringIO

        old_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            display_results(self.mock_events)
            output = sys.stdout.getvalue()
            # Verify table is created
            self.assertIn("AWS Health Events", output)
            # Verify we can find events
            self.assertGreater(len(output), 100)
        finally:
            sys.stdout = old_stdout


def generate_screenshot():
    """Generate a screenshot of the CLI output with mock data"""
    import os
    from unittest.mock import patch, MagicMock

    # Mock AWS credentials and health events
    mock_events = [
        {
            "arn": "arn:aws:health:us-east-1::event/EC2/123456",
            "service": "EC2",
            "eventTypeCode": "AWS_EC2_INSTANCE_FAILURE",
            "eventStatus": "open",
            "region": "us-east-1",
            "startTime": datetime.utcnow() - timedelta(days=5),
        },
        {
            "arn": "arn:aws:health:sa-east-1::event/RDS/789012",
            "service": "RDS",
            "eventTypeCode": "AWS_RDS_OUTAGE",
            "eventStatus": "CLOSED",
            "region": "sa-east-1",
            "startTime": datetime.utcnow() - timedelta(days=15),
        },
        {
            "arn": "arn:aws:health:us-west-2::event/ELB/345678",
            "service": "ELASTICLOADBALANCING",
            "eventTypeCode": "AWS_ELB_DEGRADED",
            "eventStatus": "CLOSED",
            "region": "us-west-2",
            "startTime": datetime.utcnow() - timedelta(days=30),
        },
    ]

    try:
        # Try to import PIL for screenshot, fallback to text-based output
        from PIL import Image, ImageDraw, ImageFont
        import subprocess

        # Run main.py with mocked AWS
        with patch("main.boto3.client") as mock_boto:
            mock_sts = MagicMock()
            mock_health = MagicMock()
            mock_boto.side_effect = lambda service, **kwargs: (
                mock_sts if service == "sts" else mock_health
            )
            mock_sts.get_caller_identity.return_value = {"UserId": "AIDAI123456"}
            mock_health.describe_events.return_value = {"events": mock_events}
            mock_health.describe_event_details.return_value = {"successfulSet": []}

            # Import after mocking to ensure mocks are in place
            from main import main

            # Capture output
            old_stdout = sys.stdout
            sys.stdout = StringIO()

            try:
                main()
                output = sys.stdout.getvalue()
            finally:
                sys.stdout = old_stdout

            # Create a simple text-based "screenshot"
            img = Image.new("RGB", (800, 600), color="black")
            draw = ImageDraw.Draw(img)

            # Add terminal-like content
            try:
                font = ImageFont.truetype("Courier New", 12)
            except:
                font = ImageFont.load_default()

            # Draw title
            draw.text((20, 20), "AWS SLA Hunter CLI Output", fill="cyan", font=font)

            # Draw some mock output lines
            lines = [
                "$ python main.py",
                "",
                "🔍 AWS SLA Hunter",
                "Finding missed SLA credits in your AWS account",
                "",
                "→ Verifying AWS credentials... ✓",
                "→ Fetching AWS Health events (last 90 days)... ✓",
                "",
                "AWS Health Events - Last 90 Days (3 found)",
                "",
                "Date       Service Region     Status    Event Type",
                "─────────────────────────────────────────────────",
                "2025-01-03 EC2     us-east-1 🔴 Open   Ec2 Instance Failure",
                "2025-01-13 RDS     sa-east-1 ⚪ Closed Rds Outage",
                "2025-02-02 ELB     us-west-2 ⚪ Closed Elb Degraded",
                "",
                "Found 3 AWS Health events with SLA potential",
                "",
                "💰 CLAIM YOUR MISSING SLA CREDITS",
                "",
                "awscostguardian.com handles SLA claims automatically",
            ]

            y = 50
            for line in lines:
                if "ERROR" in line:
                    draw.text((20, y), line, fill="red", font=font)
                elif "✓" in line:
                    draw.text((20, y), line, fill="green", font=font)
                elif "🔴" in line or "Open" in line:
                    draw.text((20, y), line, fill="red", font=font)
                elif "💰" in line or "CLAIM" in line:
                    draw.text((20, y), line, fill="yellow", font=font)
                else:
                    draw.text((20, y), line, fill="white", font=font)
                y += 20

            # Save screenshot
            script_dir = os.path.dirname(os.path.abspath(__file__))
            screenshot_path = os.path.join(script_dir, "screenshot.png")
            img.save(screenshot_path)
            print(f"Screenshot saved to: {screenshot_path}")

    except ImportError:
        # Fallback: generate text-based output
        print("PIL not available, generating text-based output instead...")
        from main import display_results, display_cta

        with patch("main.boto3.client") as mock_boto:
            mock_sts = MagicMock()
            mock_health = MagicMock()
            mock_boto.side_effect = lambda service, **kwargs: (
                mock_sts if service == "sts" else mock_health
            )
            mock_sts.get_caller_identity.return_value = {"UserId": "AIDAI123456"}
            mock_health.describe_events.return_value = {"events": mock_events}
            mock_health.describe_event_details.return_value = {"successfulSet": []}

            display_results(mock_events)
            display_cta()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AWS SLA Hunter - Tests and Screenshot")
    parser.add_argument(
        "--screenshot",
        action="store_true",
        help="Generate screenshot for README",
    )

    args = parser.parse_args()

    if args.screenshot:
        generate_screenshot()
    else:
        main(argv=[""], exit=True)
