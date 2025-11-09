#!/usr/bin/env python3
"""
AWS SLA Hunter - Find missed SLA credits in your AWS account
Detects AWS Health events with potential SLA credit eligibility
"""

import sys
import os
from datetime import datetime, timedelta
from typing import List, Dict, Any
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

# Import authentication handler
try:
    from auth_handler import AWSAuthHandler, AuthMethod
except ImportError:
    # Fallback if auth_handler not available
    AWSAuthHandler = None
    AuthMethod = None

# Fix for Windows encoding issues with emojis
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    console = Console(force_terminal=True, legacy_windows=False)
else:
    console = Console()


def get_credentials() -> bool:
    """Verify AWS credentials are available and display authentication info"""
    try:
        sts = boto3.client("sts", region_name="us-east-1")
        identity = sts.get_caller_identity()

        # Try to detect authentication method if handler available
        if AWSAuthHandler:
            auth_handler = AWSAuthHandler()
            _, method = auth_handler.detect_credentials()
            if method:
                console.print(f"[dim]({method})[/dim]", end=" ")

        return True

    except (NoCredentialsError, PartialCredentialsError):
        console.print(
            "\n[red]❌ ERROR: AWS credentials not found.[/red]\n"
            "Please configure AWS credentials using one of these methods:\n"
            "  • [bold]AWS SSO:[/bold] aws configure sso [recommended]\n"
            "  • [bold]AWS CLI:[/bold] aws configure\n"
            "  • [bold]Environment variables:[/bold] AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY\n"
            "  • [bold]IAM Role:[/bold] EC2/ECS/Lambda\n\n"
            "[cyan]Need help?[/cyan] https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html\n"
            "[cyan]Or run:[/cyan] python main.py --setup"
        )
        return False

    except ClientError as e:
        if e.response["Error"]["Code"] == "AccessDenied":
            console.print(
                "\n[red]❌ ERROR: Access denied.[/red]\n"
                "Your IAM user/role needs these permissions:\n"
                "  • health:DescribeEvents\n"
                "  • health:DescribeEventDetails\n"
                "See: https://docs.aws.amazon.com/health/latest/ug/security_iam_service-with-iam.html"
            )
        else:
            console.print(f"\n[red]❌ AWS Error: {e}[/red]")
        return False

    except Exception as e:
        console.print(f"\n[red]❌ Unexpected error: {e}[/red]")
        return False


def display_free_tier_guidance() -> None:
    """Display guidance for free tier AWS customers"""
    guidance_text = (
        "[bold cyan]📋 You're on a Free/Basic Support Plan[/bold cyan]\n\n"
        "[bold]Good news:[/bold] You have SLA credit rights!\n"
        "AWS provides SLA credits for unplanned downtime, even on free tier.\n\n"
        "[bold yellow]Your Options:[/bold yellow]\n\n"
        "[bold]Option 1: Monitor Manually (Free)[/bold]\n"
        "  1. Go to AWS Console → Health Dashboard\n"
        "  2. Check for incident reports in your regions\n"
        "  3. If you find issues, open AWS Support ticket\n"
        "  4. Claim SLA credits in the ticket\n"
        "  📄 Guide: https://aws.amazon.com/premiumsupport/knowledge-center/\n\n"
        "[bold]Option 2: Upgrade to Business Support (~$100/month)[/bold]\n"
        "  ✓ Unlock this automated SLA detection tool\n"
        "  ✓ Get 24/7 support for production issues\n"
        "  ✓ Usually pays for itself with recovered SLA credits\n"
        "  🚀 Upgrade: https://console.aws.amazon.com/support/\n\n"
        "[bold]Option 3: Use awscostguardian.com[/bold]\n"
        "  • Automates SLA detection across your account\n"
        "  • Works with any support level\n"
        "  • Free audit: https://awscostguardian.com"
    )
    console.print(Panel(guidance_text, border_style="yellow", padding=(1, 2)))


def fetch_health_events() -> List[Dict[str, Any]]:
    """Fetch AWS Health events from last 90 days"""
    try:
        health = boto3.client("health", region_name="us-east-1")

        # Calculate date range (last 90 days)
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=90)

        # Query AWS Health API
        response = health.describe_events(
            filter={
                "startTimes": [{"from": start_time, "to": end_time}],
                "eventTypeCategories": ["issue"],
                "eventStatusCodes": ["open", "closed"],
            },
            maxResults=100,
        )

        events = response.get("events", [])

        # Fetch detailed information for each event
        if events:
            event_arns = [event["arn"] for event in events]
            details_response = health.describe_event_details(eventArns=event_arns)
            details_map = {
                d["event"]["arn"]: d["eventDescription"]
                for d in details_response.get("successfulSet", [])
            }

            # Enrich events with details
            for event in events:
                if event["arn"] in details_map:
                    event["description"] = details_map[event["arn"]]

        return events

    except ClientError as e:
        if e.response["Error"]["Code"] == "SubscriptionRequiredException":
            console.print()
            display_free_tier_guidance()
        else:
            console.print(f"[red]❌ Error fetching events: {e}[/red]")
        return []


def format_event_date(event: Dict[str, Any]) -> str:
    """Format event date from event data"""
    if "startTime" in event:
        dt = event["startTime"]
        if isinstance(dt, str):
            return dt[:10]  # YYYY-MM-DD
        else:
            return dt.strftime("%Y-%m-%d")
    return "N/A"


def format_service(event: Dict[str, Any]) -> str:
    """Extract service name from event"""
    service = event.get("service", "Unknown")
    # Clean up service names
    service_map = {
        "EC2": "EC2",
        "RDS": "RDS",
        "ELASTICLOADBALANCING": "ELB",
        "S3": "S3",
        "DYNAMODB": "DynamoDB",
        "LAMBDA": "Lambda",
        "CLOUDFRONT": "CloudFront",
    }
    for key, value in service_map.items():
        if key in service.upper():
            return value
    return service[:15] if service else "Unknown"


def format_region(event: Dict[str, Any]) -> str:
    """Extract region from event"""
    region = event.get("region", "Global")
    return region if region else "Global"


def format_status(event: Dict[str, Any]) -> Text:
    """Format status with color"""
    status = event.get("eventStatus", "CLOSED")
    if status == "open":
        return Text("🔴 Open", style="bold red")
    elif status == "OPEN":
        return Text("🔴 Open", style="bold red")
    else:
        return Text("⚪ Closed", style="dim")


def format_event_type(event: Dict[str, Any]) -> str:
    """Extract and format event type"""
    event_type = event.get("eventTypeCode", "Unknown")
    # Clean up event type
    event_type = event_type.replace("_", " ").title()[:25]
    return event_type


def display_results(events: List[Dict[str, Any]]) -> None:
    """Display events in a rich table"""
    if not events:
        console.print(
            Panel(
                "[yellow]ℹ️  No SLA-eligible events found in the last 90 days.[/yellow]\n"
                "Your AWS services are running smoothly! "
                "Monitor regularly with [bold]aws-sla-hunter[/bold].",
                border_style="yellow",
                title="✓ All Good",
            )
        )
        return

    # Create table
    table = Table(
        title=f"[bold cyan]AWS Health Events - Last 90 Days ({len(events)} found)[/bold cyan]",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
        padding=(0, 1),
    )

    table.add_column("Date", style="cyan", no_wrap=True)
    table.add_column("Service", style="green", no_wrap=True)
    table.add_column("Region", style="blue", no_wrap=True)
    table.add_column("Status", justify="center")
    table.add_column("Event Type", style="yellow")

    for event in events:
        table.add_row(
            format_event_date(event),
            format_service(event),
            format_region(event),
            format_status(event),
            format_event_type(event),
        )

    console.print(table)
    console.print()

    # Display summary
    open_events = [e for e in events if e.get("eventStatus", "CLOSED").upper() == "OPEN"]
    closed_events = [
        e
        for e in events
        if e.get("eventStatus", "CLOSED").upper() in ["CLOSED", "UPCOMING"]
    ]

    summary_text = f"Found [bold yellow]{len(events)}[/bold yellow] AWS Health events with SLA potential\n"
    summary_text += (
        f"[bold red]● {len(open_events)} Open[/bold red] | [dim]⚪ {len(closed_events)} Resolved[/dim]"
    )

    console.print(Panel(summary_text, border_style="cyan", padding=(1, 2)))
    console.print()


def display_cta() -> None:
    """Display call-to-action panel"""
    cta_text = (
        "[bold cyan]💰 CLAIM YOUR MISSING SLA CREDITS[/bold cyan]\n\n"
        "aws-sla-hunter found events with [bold yellow]SLA credit potential[/bold yellow],\n"
        "but you'll need to:\n"
        "  1. Calculate financial impact\n"
        "  2. Generate formal claim documents\n"
        "  3. Open AWS support ticket\n"
        "  4. Track reimbursement\n\n"
        "[bold green]Let awscostguardian.com handle this automatically[/bold green]\n"
        "Our platform analyzes your entire account, calculates credits,\n"
        "generates claims, and tracks reimbursements.\n\n"
        "[bold]🚀 START YOUR FREE AUDIT[/bold]\n"
        "[link=https://awscostguardian.com]https://awscostguardian.com[/link]\n\n"
        "[dim]Success fee model: We only earn 30% of recovered credits[/dim]"
    )

    console.print(Panel(cta_text, border_style="bright_yellow", padding=(1, 2), width=70))


def main() -> int:
    """Main entry point"""
    # Handle --setup flag for authentication wizard
    if "--setup" in sys.argv:
        if AWSAuthHandler:
            auth_handler = AWSAuthHandler()
            success = auth_handler.setup_wizard()
            return 0 if success else 1
        else:
            console.print("[red]Error: auth_handler module not available[/red]")
            return 1

    console.print(
        Panel(
            "[bold cyan]🔍 AWS SLA Hunter[/bold cyan]\n"
            "[dim]Finding missed SLA credits in your AWS account[/dim]",
            border_style="cyan",
            padding=(1, 2),
        )
    )
    console.print()

    # Step 1: Verify credentials
    console.print("[cyan]→[/cyan] Verifying AWS credentials...", end=" ")
    if not get_credentials():
        console.print()
        return 1
    console.print("[green]✓[/green]")
    console.print()

    # Step 2: Fetch events
    console.print("[cyan]→[/cyan] Fetching AWS Health events (last 90 days)...", end=" ")
    events = fetch_health_events()
    console.print("[green]✓[/green]")
    console.print()

    # Step 3: Display results
    display_results(events)

    # Step 4: Call to action
    display_cta()

    return 0


if __name__ == "__main__":
    sys.exit(main())
