# ============================================================
# core/intent_parser.py — Intent Detection Engine
# Reads the user's message and classifies what they want.
# Returns: "automation", "chat", or "exit"
# ============================================================

from automation.commands import COMMAND_MAP  # Import known command keywords


def parse_intent(user_input: str) -> dict:
    """
    Analyzes the user's input and determines their intent.

    Returns a dict like:
        { "type": "automation", "command": "open_browser" }
        { "type": "chat" }
        { "type": "exit" }
    """

    # Normalize input: lowercase + strip whitespace
    text = user_input.strip().lower()

    # --- Check for EXIT intent ---
    exit_phrases = ["exit", "quit", "bye", "goodbye", "shut down", "stop", "close tulen"]
    if any(phrase in text for phrase in exit_phrases):
        return {"type": "exit"}

    # --- Check for AUTOMATION intent ---
    # Loop through every known command and its trigger keywords
    for command_name, command_info in COMMAND_MAP.items():
        triggers = command_info.get("triggers", [])
        for trigger in triggers:
            if trigger in text:
                # Found a matching command!
                return {
                    "type": "automation",
                    "command": command_name,
                    "raw_input": user_input
                }

    # --- Default: CHAT intent ---
    # If nothing matched, treat it as a conversation
    return {
        "type": "chat",
        "raw_input": user_input
    }
