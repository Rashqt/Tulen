# ============================================================
# ui/cli.py — Command-Line Interface
# Handles all terminal display: colors, formatting, prompts.
# This is the ONLY place where print() calls for UI should live.
# ============================================================

from colorama import Fore, Style, init as colorama_init

# Initialize colorama (required on Windows for ANSI color support)
colorama_init(autoreset=True)


def print_banner():
    """
    Prints Tulen's startup banner.
    """
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════╗
║                                          ║
║    🌷  T U L E N  — AI Assistant  🌷    ║
║                                          ║
║    Type your message and press Enter.    ║
║    Say 'exit' or 'quit' to stop.         ║
║                                          ║
╚══════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)


def print_tulen(message: str):
    """
    Prints Tulen's response with her name label.
    """
    print(f"\n{Fore.CYAN}🌷 Tulen:{Style.RESET_ALL} {message}\n")


def print_system(message: str):
    """
    Prints a system/status message (dimmer color).
    """
    print(f"{Fore.YELLOW}  ⚙  {message}{Style.RESET_ALL}")


def print_error(message: str):
    """
    Prints an error message in red.
    """
    print(f"{Fore.RED}  ✖  {message}{Style.RESET_ALL}")


def print_action(message: str):
    """
    Prints an automation action notice.
    """
    print(f"{Fore.GREEN}  ▶  {message}{Style.RESET_ALL}")


def get_user_input(prompt: str = "You → ") -> str:
    """
    Gets input from the user with a styled prompt.
    Returns the raw input string.
    """
    try:
        user_text = input(f"{Fore.WHITE}{prompt}{Style.RESET_ALL}").strip()
        return user_text
    except (EOFError, KeyboardInterrupt):
        # Handle Ctrl+C or piped input gracefully
        return "exit"
