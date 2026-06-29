import argparse
import argparse

from promptshield.client import PromptShield
from promptshield.exceptions import (
    APIConnectionError,
    APIResponseError,
)

def print_header(title):
    print(f"\n=== {title} ===")
    print("-" * 42)


def print_footer():
    print("-" * 42)


def format_action(action):
    if action.upper() == "ALLOW":
        return "[ALLOW]"

    if action.upper() == "BLOCK":
        return "[BLOCK]"

    return action


def format_status(status):
    if status.lower() == "healthy":
        return "[HEALTHY]"

    return f"[{status.upper()}]"


def handle_scan(args):
    """
    Scan a prompt using PromptShield backend.
    """

    shield = PromptShield()

    try:
        result = shield.scan(args.prompt)

        print_header("PromptShield Security Scan")

        print(f"Attack Type : {result.attack_type.upper()}")
        print(f"Confidence  : {result.confidence * 100:.2f}%")
        print(f"Risk Score  : {result.risk_score}")
        print(f"Action      : {format_action(result.action)}")

        print_footer()

    except APIConnectionError as e:
        print(f"Connection Error: {e}")

    except APIResponseError as e:
        print(f"API Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


def handle_chat(args):
    """
    Chat with an LLM through PromptShield.
    """

    shield = PromptShield()

    try:
        result = shield.chat(args.prompt)

        print_header("PromptShield Chat")

        if result.response:
            print(result.response)
        else:
            print("Request blocked by PromptShield.")

        print()

        print(f"Action      : {format_action(result.action)}")
        print(f"Attack Type : {result.attack_type.upper()}")
        print(f"Risk Score  : {result.risk_score}")

        print_footer()

    except APIConnectionError as e:
        print(f"Connection Error: {e}")

    except APIResponseError as e:
        print(f"API Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


def handle_health(args):
    """
    Check PromptShield backend health.
    """

    shield = PromptShield()

    try:
        health = shield.health()

        print_header("PromptShield Health")

        print(f"Status      : {format_status(health.status)}")
        print(f"Version     : {health.version}")
        print(f"Provider    : {health.provider}")

        print_footer()

    except APIConnectionError as e:
        print(f"Connection Error: {e}")

    except APIResponseError as e:
        print(f"API Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        prog="promptshield",
        description="PromptShield Security CLI",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show PromptShield version",
    )

    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
    )

    # -----------------------------
    # scan
    # -----------------------------
    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a prompt for attacks",
    )

    scan_parser.add_argument(
        "prompt",
        help="Prompt to scan",
    )

    scan_parser.set_defaults(func=handle_scan)

    # -----------------------------
    # chat
    # -----------------------------
    chat_parser = subparsers.add_parser(
        "chat",
        help="Chat through PromptShield",
    )

    chat_parser.add_argument(
        "prompt",
        help="Prompt to send",
    )

    chat_parser.set_defaults(func=handle_chat)

    # -----------------------------
    # health
    # -----------------------------
    health_parser = subparsers.add_parser(
        "health",
        help="Check PromptShield server",
    )

    health_parser.set_defaults(func=handle_health)

    # -----------------------------
    # Parse arguments
    # -----------------------------
    args = parser.parse_args()

    if args.version:
        print("PromptShield CLI v1.0.0")
        return

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()