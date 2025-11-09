#!/usr/bin/env python3
"""
Test script to simulate free tier user experience
Shows what a free tier customer sees when running the tool
"""

import sys
import os
from rich.console import Console
from rich.panel import Panel

# Fix for Windows encoding issues
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    console = Console(force_terminal=True, legacy_windows=False)
else:
    console = Console()


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


def main():
    """Simulate free tier user running the tool"""
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
    console.print("[green]✓[/green]")
    console.print()

    # Step 2: Fetch events (will fail for free tier)
    console.print("[cyan]→[/cyan] Fetching AWS Health events (last 90 days)...", end=" ")
    console.print("[green]✓[/green]")
    console.print()

    # Step 3: Display guidance (simulating the error response)
    display_free_tier_guidance()

    return 0


if __name__ == "__main__":
    sys.exit(main())
