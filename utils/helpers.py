# ============================================================
# utils/helpers.py — Utility / Helper Functions
# Small reusable functions that don't belong to any specific module.
# ============================================================

import datetime


def get_time_greeting() -> str:
    """
    Returns a time-appropriate greeting word.
    e.g., "Good morning", "Good afternoon", "Good evening"
    """
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"


def get_current_time() -> str:
    """
    Returns the current time as a formatted string.
    e.g., "3:45 PM"
    """
    return datetime.datetime.now().strftime("%I:%M %p")


def get_current_date() -> str:
    """
    Returns today's date as a formatted string.
    e.g., "Monday, April 13, 2026"
    """
    return datetime.datetime.now().strftime("%A, %B %d, %Y")


def sanitize_input(text: str) -> str:
    """
    Cleans up raw user input.
    - Strips leading/trailing whitespace
    - Collapses multiple spaces
    """
    return " ".join(text.split())


def truncate(text: str, max_length: int = 200) -> str:
    """
    Truncates long text for display purposes.
    Adds '...' if the text was cut.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length].rstrip() + "..."
