# ============================================================
# core/decision_engine.py — Decision Engine
# Takes a parsed intent and decides what to DO with it.
# Routes to: AI response, automation, or exit.
# ============================================================

from automation.executor import execute_command


def decide(intent: dict, ai_response_func) -> dict:
    """
    Takes a parsed intent and produces an action result.

    Args:
        intent: The dict from intent_parser.parse_intent()
                e.g. {"type": "automation", "command": "open_browser"}
        ai_response_func: A callable that takes user text and returns AI response string

    Returns:
        A dict with:
            "action": what was done ("chat", "automation", "exit")
            "response": the text response to show/speak
    """

    intent_type = intent.get("type")

    # --- Handle AUTOMATION commands ---
    if intent_type == "automation":
        command_name = intent.get("command")
        response_message = execute_command(command_name)
        return {
            "action": "automation",
            "response": response_message
        }

    # --- Handle CHAT / conversation ---
    elif intent_type == "chat":
        user_text = intent.get("raw_input", "")
        ai_reply = ai_response_func(user_text)  # Call the brain's AI function
        return {
            "action": "chat",
            "response": ai_reply
        }

    # --- Handle EXIT ---
    elif intent_type == "exit":
        return {
            "action": "exit",
            "response": None  # Farewell is handled by main.py
        }

    # --- Fallback for unknown intents ---
    else:
        return {
            "action": "chat",
            "response": "I'm not sure what you meant. Could you rephrase that?"
        }
