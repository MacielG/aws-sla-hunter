#!/usr/bin/env python3
"""
AWS Authentication Handler
Provides intelligent credential detection and setup wizard
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any, Tuple
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich import box

# Fix for Windows encoding issues with emojis
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    console = Console(force_terminal=True, legacy_windows=False)
else:
    console = Console()


class AuthMethod:
    """Enum-like class for authentication methods"""
    IAM_ROLE = "IAM Role (EC2/ECS/Lambda)"
    ENV_VARS = "Environment Variables"
    AWS_CREDENTIALS_FILE = "~/.aws/credentials"
    AWS_SSO = "AWS SSO"
    MANUAL_SETUP = "Manual Setup"
    UNKNOWN = "Unknown"


class AWSAuthHandler:
    """Handles AWS authentication with multiple methods and fallbacks"""

    def __init__(self):
        self.console = console
        self.detected_method = None
        self.credentials_location = None

    def get_credentials_priority_order(self) -> list:
        """Return the order in which boto3 looks for credentials"""
        return [
            ("IAM Role", self._check_iam_role),
            ("Environment Variables", self._check_env_vars),
            ("AWS Credentials File", self._check_credentials_file),
            ("AWS SSO", self._check_sso),
        ]

    def _check_iam_role(self) -> Tuple[bool, Optional[str]]:
        """Check if running with IAM Role (EC2/ECS/Lambda)"""
        try:
            # Try to get metadata from EC2 metadata service
            import urllib.request
            urllib.request.urlopen("http://169.254.169.254/latest/meta-data/", timeout=1)
            return True, AuthMethod.IAM_ROLE
        except Exception:
            return False, None

    def _check_env_vars(self) -> Tuple[bool, Optional[str]]:
        """Check if AWS credentials are in environment variables"""
        if os.getenv("AWS_ACCESS_KEY_ID") and os.getenv("AWS_SECRET_ACCESS_KEY"):
            return True, AuthMethod.ENV_VARS
        return False, None

    def _check_credentials_file(self) -> Tuple[bool, Optional[str]]:
        """Check if ~/.aws/credentials file exists and has profiles"""
        creds_file = Path.home() / ".aws" / "credentials"
        if creds_file.exists():
            return True, AuthMethod.AWS_CREDENTIALS_FILE
        return False, None

    def _check_sso(self) -> Tuple[bool, Optional[str]]:
        """Check if AWS SSO is configured"""
        config_file = Path.home() / ".aws" / "config"
        if config_file.exists():
            try:
                with open(config_file) as f:
                    content = f.read()
                    if "sso_start_url" in content or "sso_account_id" in content:
                        return True, AuthMethod.AWS_SSO
            except Exception:
                pass
        return False, None

    def detect_credentials(self) -> Tuple[bool, Optional[str]]:
        """
        Try to detect existing AWS credentials
        Returns: (has_credentials, auth_method_used)
        """
        try:
            sts = boto3.client("sts", region_name="us-east-1")
            identity = sts.get_caller_identity()

            # Detect which method was used
            for method_name, check_func in self.get_credentials_priority_order():
                has_creds, method = check_func()
                if has_creds:
                    self.detected_method = method
                    return True, method

            # If no specific method detected, credentials exist but method unknown
            self.detected_method = AuthMethod.UNKNOWN
            return True, AuthMethod.UNKNOWN

        except (NoCredentialsError, PartialCredentialsError):
            return False, None
        except ClientError as e:
            if e.response["Error"]["Code"] == "InvalidClientTokenId":
                return False, "Expired Credentials"
            raise
        except Exception as e:
            console.print(f"[yellow]Warning: Could not detect credentials: {e}[/yellow]")
            return False, None

    def display_current_auth(self, method: str, identity: Dict[str, Any] = None) -> None:
        """Display current authentication status"""
        auth_info = f"[bold cyan]✓ Authentication Method[/bold cyan]\n{method}"

        if identity:
            auth_info += f"\n[dim]Account: {identity.get('Account', 'N/A')}[/dim]"
            auth_info += f"\n[dim]User: {identity.get('Arn', 'N/A')}[/dim]"

        self.console.print(Panel(auth_info, border_style="green", padding=(1, 1)))

    def setup_wizard(self) -> bool:
        """
        Interactive setup wizard for AWS credentials
        Returns: True if setup successful
        """
        self.console.print()
        self.console.print(
            Panel(
                "[bold cyan]🔐 AWS Authentication Setup[/bold cyan]\n"
                "[dim]Let's configure your AWS credentials securely[/dim]",
                border_style="cyan",
                padding=(1, 2),
            )
        )
        self.console.print()

        self.console.print("[cyan]Checking for existing credentials...[/cyan]")
        has_creds, method = self.detect_credentials()

        if has_creds:
            self.console.print(f"[green]✓ Found credentials using: {method}[/green]")
            self.console.print()

            # Show details
            try:
                sts = boto3.client("sts", region_name="us-east-1")
                identity = sts.get_caller_identity()
                self.display_current_auth(method, identity)
                return True
            except Exception as e:
                self.console.print(f"[yellow]Warning: Could not verify credentials: {e}[/yellow]")
                return False

        # No existing credentials found
        self.console.print("[yellow]⚠️  No AWS credentials found[/yellow]")
        self.console.print()

        options = [
            ("1", "AWS SSO (Recommended - Browser login, secure)", self._setup_sso),
            ("2", "AWS CLI Configuration (Manual entry)", self._setup_manual),
            ("3", "Environment Variables (.env file)", self._setup_env_file),
            ("4", "Skip for now", None),
        ]

        self.console.print("[bold]Choose authentication method:[/bold]")
        for num, desc, _ in options:
            self.console.print(f"  {num}. {desc}")
        self.console.print()

        choice = Prompt.ask("Select option", choices=["1", "2", "3", "4"], default="1")

        if choice == "4":
            self.console.print(
                "[yellow]Skipping setup. Configure manually later with: aws configure[/yellow]"
            )
            return False

        for num, _, handler in options:
            if num == choice:
                if handler:
                    return handler()
                return False

        return False

    def _setup_sso(self) -> bool:
        """Setup AWS SSO"""
        self.console.print()
        self.console.print(
            Panel(
                "[bold cyan]AWS SSO Setup[/bold cyan]\n\n"
                "This will open AWS in your browser.\n"
                "Follow the prompts to authenticate securely.\n\n"
                "[dim]Your credentials will be saved automatically.[/dim]",
                border_style="cyan",
                padding=(1, 2),
            )
        )

        if not Confirm.ask("\nProceed with AWS SSO setup?"):
            return False

        try:
            self.console.print("[cyan]Launching AWS SSO setup...[/cyan]")
            result = subprocess.run(
                ["aws", "configure", "sso"], capture_output=False, text=True
            )

            if result.returncode == 0:
                self.console.print("[green]✓ AWS SSO configured successfully![/green]")
                self.console.print()

                # Verify credentials
                has_creds, method = self.detect_credentials()
                if has_creds:
                    self.console.print(f"[green]✓ Verified: Using {method}[/green]")
                    return True
            else:
                self.console.print("[red]✗ AWS SSO setup failed[/red]")
                return False

        except FileNotFoundError:
            self.console.print(
                "[red]Error: AWS CLI not found[/red]\n"
                "Install it from: https://aws.amazon.com/cli/"
            )
            return False
        except Exception as e:
            self.console.print(f"[red]Error during SSO setup: {e}[/red]")
            return False

    def _setup_manual(self) -> bool:
        """Setup AWS CLI manually"""
        self.console.print()
        self.console.print(
            Panel(
                "[bold cyan]AWS CLI Manual Setup[/bold cyan]\n\n"
                "This will use 'aws configure' to set up your credentials.\n"
                "You'll need your AWS Access Key ID and Secret Access Key.\n\n"
                "[yellow]Get your credentials:[/yellow]\n"
                "https://console.aws.amazon.com/iam/home#/security_credentials",
                border_style="cyan",
                padding=(1, 2),
            )
        )

        if not Confirm.ask("\nProceed with manual configuration?"):
            return False

        try:
            self.console.print("[cyan]Launching AWS CLI configuration...[/cyan]")
            result = subprocess.run(
                ["aws", "configure"], capture_output=False, text=True
            )

            if result.returncode == 0:
                self.console.print("[green]✓ AWS credentials configured![/green]")
                self.console.print()

                # Verify
                has_creds, method = self.detect_credentials()
                if has_creds:
                    self.console.print(f"[green]✓ Verified: Using {method}[/green]")
                    return True
            else:
                self.console.print("[red]✗ AWS configuration failed[/red]")
                return False

        except FileNotFoundError:
            self.console.print(
                "[red]Error: AWS CLI not found[/red]\n"
                "Install it from: https://aws.amazon.com/cli/"
            )
            return False
        except Exception as e:
            self.console.print(f"[red]Error: {e}[/red]")
            return False

    def _setup_env_file(self) -> bool:
        """Setup environment variables in .env file"""
        self.console.print()
        self.console.print(
            Panel(
                "[bold cyan].env File Setup[/bold cyan]\n\n"
                "[yellow]Get your AWS credentials:[/yellow]\n"
                "https://console.aws.amazon.com/iam/home#/security_credentials\n\n"
                "[dim]Warning: Keep .env file secret, add to .gitignore[/dim]",
                border_style="cyan",
                padding=(1, 2),
            )
        )

        env_file = Path(".env")

        access_key = Prompt.ask("AWS Access Key ID")
        secret_key = Prompt.ask("AWS Secret Access Key", password=True)
        region = Prompt.ask("AWS Region (default: us-east-1)", default="us-east-1")

        # Create .env file
        env_content = f"""# AWS Credentials (Automatically configured)
AWS_ACCESS_KEY_ID={access_key}
AWS_SECRET_ACCESS_KEY={secret_key}
AWS_DEFAULT_REGION={region}

# Optional: Session token (if using temporary credentials)
# AWS_SESSION_TOKEN=your_session_token_here
"""

        env_file.write_text(env_content)
        os.chmod(env_file, 0o600)  # Make file readable only by owner

        self.console.print(f"[green]✓ Credentials saved to .env[/green]")
        self.console.print("[dim]Make sure .env is in .gitignore[/dim]")

        # Verify
        has_creds, method = self.detect_credentials()
        if has_creds:
            self.console.print(f"[green]✓ Verified: Using {method}[/green]")
            return True

        return False

    def verify_health_api_access(self) -> Tuple[bool, Optional[str]]:
        """
        Verify that credentials have access to AWS Health API
        Returns: (has_access, error_message)
        """
        try:
            health = boto3.client("health", region_name="us-east-1")
            # Try a simple describe_events call
            health.describe_events(maxResults=1)
            return True, None
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "SubscriptionRequiredException":
                return False, "AWS Health API requires Business or Enterprise Support"
            elif error_code == "AccessDenied":
                return False, "IAM permissions missing (need health:DescribeEvents)"
            else:
                return False, str(e)
        except Exception as e:
            return False, str(e)
