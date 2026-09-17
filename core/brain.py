# ============================================================
# core/brain.py — Tulen's Brain (Central Orchestrator)
# This is the main hub. It connects:
#   intent_parser → decision_engine → AI or automation
# It also manages the Claude AI API connection.
# ============================================================

import anthropic
from config import ANTHROPIC_API_KEY, AI_MODEL, MAX_TOKENS, SHOW_THINKING
from core.personality import get_system_prompt, get_error_message
from core.intent_parser import parse_intent
from core.decision_engine import decide


class TulenBrain:
    """
    The central brain of Tulen.
    Handles AI communication and orchestrates all subsystems.
    """

    def __init__(self):
        # Initialize the Anthropic Claude client
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        # The system prompt defines Tulen's personality
        self.system_prompt = get_system_prompt()

        # Conversation history — lets Tulen remember the current session
        # Format: [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
        self.conversation_history = []

        print("[Brain] Tulen's brain initialized.")

    def ask_ai(self, user_text: str) -> str:
        """
        Sends a message to Claude AI and returns the response.
        Maintains conversation history for context within a session.
        """
        # Add the user's message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_text
        })

        try:
            # Call the Claude API
            response = self.client.messages.create(
                model=AI_MODEL,
                max_tokens=MAX_TOKENS,
                system=self.system_prompt,
                messages=self.conversation_history
            )

            # Extract the text from the response
            ai_reply = response.content[0].text

            # Add Tulen's reply to history (so she remembers the conversation)
            self.conversation_history.append({
                "role": "assistant",
                "content": ai_reply
            })

            return ai_reply

        except anthropic.AuthenticationError:
            return "My API key seems invalid. Please check the config file."

        except anthropic.APIConnectionError:
            return "I can't reach the AI servers right now. Check your internet connection."

        except anthropic.RateLimitError:
            return "I've hit the rate limit. Give me a moment before asking again."

        except Exception as e:
            print(f"[Brain] Unexpected AI error: {e}")
            return get_error_message()

    def process(self, user_input: str) -> dict:
        """
        Main processing pipeline. Takes raw user input and returns a result dict.

        Flow:
            user_input → parse_intent → decide → result

        Returns:
            dict with "action" and "response" keys
        """
        # Step 1: Parse what the user wants
        intent = parse_intent(user_input)

        if SHOW_THINKING:
            print(f"[Brain] Detected intent: {intent}")

        # Step 2: Decide what to do and execute
        result = decide(intent, ai_response_func=self.ask_ai)

        return result

    def clear_history(self):
        """
        Clears conversation history. Tulen forgets the current session.
        """
        self.conversation_history = []
        print("[Brain] Conversation history cleared.")
