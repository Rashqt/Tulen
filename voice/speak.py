# ============================================================
# voice/speak.py — Text-to-Speech Output
# Uses pyttsx3 (offline TTS) to make Tulen speak responses.
# No internet required. Works on Windows, macOS, and Linux.
# ============================================================

import pyttsx3
from config import VOICE_ENABLED, VOICE_RATE, VOICE_VOLUME, VOICE_INDEX


# Initialize the TTS engine once at module load
# (Avoid re-initializing on every speak call — it's slow)
_engine = None


def _get_engine():
    """
    Returns the TTS engine, initializing it if needed.
    Uses a module-level singleton to avoid repeated init.
    """
    global _engine

    if _engine is None:
        try:
            _engine = pyttsx3.init()

            # Set speaking rate (words per minute)
            _engine.setProperty("rate", VOICE_RATE)

            # Set volume (0.0 to 1.0)
            _engine.setProperty("volume", VOICE_VOLUME)

            # Set voice (try different indexes for different voices)
            voices = _engine.getProperty("voices")
            if voices and VOICE_INDEX < len(voices):
                _engine.setProperty("voice", voices[VOICE_INDEX].id)

        except Exception as e:
            print(f"[Voice] Could not initialize TTS engine: {e}")
            _engine = None

    return _engine


def speak(text: str):
    """
    Makes Tulen speak the given text out loud.

    Args:
        text: The string to speak aloud

    If VOICE_ENABLED is False in config, this function does nothing.
    If TTS fails, it silently falls back to text-only mode.
    """

    # Respect the config setting
    if not VOICE_ENABLED:
        return

    # Get the TTS engine
    engine = _get_engine()

    if engine is None:
        # TTS isn't available — graceful fallback
        return

    try:
        engine.say(text)
        engine.runAndWait()  # Block until speech is complete

    except RuntimeError:
        # Sometimes the engine gets into a bad state — reset it
        global _engine
        _engine = None

    except Exception as e:
        print(f"[Voice] Speech error: {e}")


def list_voices():
    """
    Utility: Prints all available TTS voices on this system.
    Run this if you want to find better voice options.
    """
    engine = _get_engine()
    if engine:
        voices = engine.getProperty("voices")
        print("\n--- Available Voices ---")
        for i, voice in enumerate(voices):
            print(f"  [{i}] {voice.name} | {voice.id}")
        print("------------------------\n")
    else:
        print("[Voice] TTS engine not available.")
