# wake_stt.py
# Minimal example: fallback to continuous STT if porcupine not available.
import os
import queue
import sounddevice as sd
import whisper
from dotenv import load_dotenv
load_dotenv()


MODEL_NAME = os.getenv('WHISPER_MODEL', 'small')
print('Loading Whisper model', MODEL_NAME)
model = whisper.load_model(MODEL_NAME)


q = queue.Queue()


def callback(indata, frames, time, status):
if status:
print(status)
q.put(indata.copy())


print('Starting microphone. Say "Tiulen" to wake (manual detection demo).')
with sd.InputStream(channels=1, samplerate=16000, callback=callback):
while True:
audio = q.get()
# write temp wav
import numpy as np
from scipy.io.wavfile import write
tmp = 'tmp_in.wav'
write(tmp, 16000, audio)
res = model.transcribe(tmp)
text = res.get('text','').strip()
if text:
print('Heard:', text)
if 'tiulen' in text.lower():
print('--> Wake word detected')
# record next phrase and transcribe
print('Record your command (5s)...')
import time
rec = sd.rec(int(16000*5), samplerate=16000, channels=1)
sd.wait()
write('cmd.wav', 16000, rec)
cmd = model.transcribe('cmd.wav').get('text','')
print('Command:', cmd)