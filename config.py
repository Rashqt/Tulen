# ============================================================
# config.py — Central configuration for Tulen
# All settings live here. Change these to customize Tulen.
# ============================================================

# --- Assistant Identity ---
ASSISTANT_NAME = "Tulen"
USER_NAME = "Boss"  # Change this to your name

# --- AI Model Settings ---
# Uses Anthropic Claude API
# Set your API key here OR use an environment variable (recommended)
import os
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "your-api-key-here")
AI_MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 512  # Keep responses concise

# --- Voice Settings ---
VOICE_ENABLED = True       # Set False to disable TTS (text-only mode)
VOICE_RATE = 175           # Speaking speed (words per minute)
VOICE_VOLUME = 1.0         # Volume: 0.0 (silent) to 1.0 (max)
# Voice gender preference: 0 = first available, try 1 for female on some systems
VOICE_INDEX = 0

# --- Behavior Settings ---
SHOW_THINKING = False      # Set True to see intent detection logs
CLI_PROMPT = "You → "     # The prompt symbol in the terminal

# --- Platform Detection ---
import platform
CURRENT_OS = platform.system()  # "Windows", "Darwin" (macOS), or "Linux"
