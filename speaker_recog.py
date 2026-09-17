# speaker_recog.py
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np


encoder = VoiceEncoder()


def enroll(path_to_audio):
wav = preprocess_wav(path_to_audio)
embed = encoder.embed_utterance(wav)
return embed


def similarity(e1, e2):
return np.dot(e1, e2) / (np.linalg.norm(e1)*np.linalg.norm(e2))


if __name__ == '__main__':
# Example: enroll owner
owner = enroll('owner_sample.wav')
candidate = enroll('candidate.wav')
print('similarity:', similarity(owner, candidate))