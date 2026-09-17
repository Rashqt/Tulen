# ============================================================
# automation/executor.py — Desktop Command Executor
# Takes a command name, finds the right shell command,
# and runs it safely using subprocess.
# ============================================================

import subprocess
from automation.commands import get_command_for_os
from core.personality import get_error_message


def execute_command(command_name: str) -> str:
    """
    Executes a desktop automation command by name.

    Args:
        command_name: The command key from COMMAND_MAP (e.g., "open_browser")

    Returns:
        A string message describing what happened (for Tulen to say/display)
    """

    # Step 1: Get the OS-specific command details
    cmd_info = get_command_for_os(command_name)

    # Step 2: Handle unknown commands
    if cmd_info is None:
        return f"I don't have a command mapped for '{command_name}' yet."

    shell_command = cmd_info["shell_command"]
    response_message = cmd_info["message"]

    # Step 3: Handle commands with no OS-specific implementation
    if not shell_command:
        return f"This command isn't supported on your operating system yet."

    # Step 4: Run the command safely
    try:
        subprocess.Popen(
            shell_command,
            shell=True,               # Allow shell syntax like 'start chrome'
            stdout=subprocess.DEVNULL, # Suppress output clutter
            stderr=subprocess.DEVNULL  # Suppress error clutter
        )
        return response_message

    except FileNotFoundError:
        # The app/program wasn't found on the system
        return f"I couldn't find that application on your system. It may not be installed."

    except PermissionError:
        # No permission to run this
        return f"I don't have permission to run that command."

    except Exception as e:
        # Any other unexpected error
        return f"Something went wrong while executing the command: {str(e)}"
