# tts_switcher.py
import os
from dotenv import load_dotenv
load_dotenv()
ELEVEN_KEY = os.getenv('ELEVEN_API_KEY','')


def eleven_tts(text,