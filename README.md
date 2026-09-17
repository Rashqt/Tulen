# Tiulen — Full Starter Kit


**What this repo contains**
- `main.py` — orchestrator: chat loop, mode switching, command handling
- `wake_stt.py` — wake-word listener and STT integration (Whisper)
- `speaker_recog.py` — speaker enrollment + verification demo (Resemblyzer)
- `tts_switcher.py` — TTS wrapper (ElevenLabs + Coqui fallback)
- `commands.py` — master-control command handlers
- `secure_destroy.py` — AES encryption of data and secure key deletion
- `gui/app.py` + `gui/static/index.html` — minimal Flask GUI with avatar and mode buttons
- `personality.json` — Tiulen personality and modes


## Quick start


1. Create a Python venv and activate it:


```bash
python -m venv venv
# mac/linux
source venv/bin/activate
# windows
.\venv\Scripts\Activate.ps1