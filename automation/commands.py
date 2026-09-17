# ============================================================
# automation/commands.py — Command Definitions
# Maps command names to trigger phrases and execution details.
# Add new commands here to expand Tulen's capabilities.
# ============================================================

import config

# -------------------------------------------------------
# COMMAND_MAP: The master list of all automation commands
#
# Structure per command:
#   "command_name": {
#       "triggers": [list of phrases that activate this command],
#       "windows":  command/path to run on Windows,
#       "darwin":   command/path to run on macOS,
#       "linux":    command/path to run on Linux,
#       "message":  what Tulen says when running this command
#   }
# -------------------------------------------------------

COMMAND_MAP = {

    # --- Web Browser ---
    "open_browser": {
        "triggers": ["open browser", "open chrome", "open firefox", "launch browser", "open internet"],
        "windows": "start chrome",
        "darwin": "open -a 'Google Chrome'",
        "linux": "xdg-open https://www.google.com",
        "message": "Opening your browser."
    },

    # --- File Manager ---
    "open_files": {
        "triggers": ["open files", "open file manager", "open explorer", "open finder", "show files"],
        "windows": "explorer",
        "darwin": "open .",
        "linux": "xdg-open ~",
        "message": "Opening file manager."
    },

    # --- Notepad / Text Editor ---
    "open_notepad": {
        "triggers": ["open notepad", "open text editor", "open notes", "launch notepad"],
        "windows": "notepad",
        "darwin": "open -a TextEdit",
        "linux": "gedit",
        "message": "Opening text editor."
    },

    # --- Calculator ---
    "open_calculator": {
        "triggers": ["open calculator", "launch calculator", "open calc"],
        "windows": "calc",
        "darwin": "open -a Calculator",
        "linux": "gnome-calculator",
        "message": "Pulling up the calculator."
    },

    # --- Terminal ---
    "open_terminal": {
        "triggers": ["open terminal", "open command prompt", "open cmd", "launch terminal", "open console"],
        "windows": "start cmd",
        "darwin": "open -a Terminal",
        "linux": "x-terminal-emulator",
        "message": "Opening terminal."
    },

    # --- System Settings ---
    "open_settings": {
        "triggers": ["open settings", "open system settings", "open control panel", "system preferences"],
        "windows": "start ms-settings:",
        "darwin": "open -a 'System Preferences'",
        "linux": "gnome-control-center",
        "message": "Opening system settings."
    },

    # --- Screenshot ---
    "screenshot": {
        "triggers": ["take screenshot", "capture screen", "screenshot", "take a screenshot"],
        "windows": "snippingtool",
        "darwin": "screencapture -i ~/Desktop/screenshot.png",
        "linux": "gnome-screenshot",
        "message": "Taking a screenshot."
    },

    # --- Lock Screen ---
    "lock_screen": {
        "triggers": ["lock screen", "lock the screen", "lock computer", "lock my computer"],
        "windows": "rundll32.exe user32.dll,LockWorkStation",
        "darwin": "pmset displaysleepnow",
        "linux": "gnome-screensaver-command -l",
        "message": "Locking your screen. Stay safe."
    },

    # --- Google Search (opens browser with search) ---
    "google_search": {
        "triggers": ["search for", "google", "look up", "search google"],
        "windows": "start https://www.google.com",
        "darwin": "open https://www.google.com",
        "linux": "xdg-open https://www.google.com",
        "message": "Opening Google for you."
    },

    # --- YouTube ---
    "open_youtube": {
        "triggers": ["open youtube", "launch youtube", "go to youtube"],
        "windows": "start https://www.youtube.com",
        "darwin": "open https://www.youtube.com",
        "linux": "xdg-open https://www.youtube.com",
        "message": "Opening YouTube."
    },

}


def get_command_for_os(command_name: str) -> dict | None:
    """
    Returns the full command info for the current OS.
    Returns None if the command doesn't exist.
    """
    if command_name not in COMMAND_MAP:
        return None

    cmd_info = COMMAND_MAP[command_name]
    os_key = config.CURRENT_OS.lower()  # "windows", "darwin", or "linux"

    # Get the OS-specific shell command
    shell_command = cmd_info.get(os_key)

    return {
        "shell_command": shell_command,
        "message": cmd_info.get("message", "Done.")
    }
