from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from functools import reduce
import os

def trim_silence(audio):
    ns = detect_nonsilent(audio, min_silence_len=400, silence_thresh=-38)  # parameters may need adjusting
    segments = [audio[start:end] for start, end in ns]
    return reduce(lambda a, b: a + b, segments)

# Go through all .wav files in the directory
directory = "audio_text_pairs"
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        path = os.path.join(directory, filename)
        audio = AudioSegment.from_wav(path)
        trimmed_audio = trim_silence(audio)
        trimmed_audio.export(path, format="wav")
