# Atlas Voice Script

Introducing our comprehensive audio recording and processing tool! This software is a powerful blend of user-friendly interactions and efficient audio manipulations that empower you to record, save, play, and process audio in a streamlined manner. Built using advanced Python libraries such as `gradio`, `sounddevice`, `soundfile`, `numpy`, and `pydub`, it allows you to record your voice, associate each recording with a unique text from a predefined file, and save these pairs for easy reference. But it doesn't stop there! The software also efficiently processes each recorded audio file to eliminate silent portions, ensuring your recordings are clear and concise. Whether you're working on a speech recognition project, building a voiceover portfolio, or exploring the realm of digital sound, this software provides you with the tools to achieve your audio goals. Jump in and experience the seamless harmony of intuitive user interfaces and powerful audio processing!

## Required Libraries

To run these scripts, you'll need the following libraries outside the basic Python libraries:

- `gradio` - For creating the user interface.
- `sounddevice` - For recording audio from the microphone.
- `soundfile` - For reading and writing sound files.
- `numpy` - For numerical computations (used here for creating the array to hold the recording).
- `pydub` - For manipulating audio files (used here for trimming silence from audio).

Please ensure these libraries are installed in your Python environment before running these scripts. You can install them using pip:

```bash
pip install gradio sounddevice soundfile numpy pydub
```
## atlas-voice.py

This script creates an interface using the Gradio library that allows users to record audio from their microphone and save the recordings as .wav files. Each recording is paired with a line of text from the voice.txt file. The audio and text pairs are saved in the audio_text_pairs directory.

Here's a detailed walkthrough of the code:

Import necessary libraries - gradio, sounddevice, soundfile, numpy, and os.
Read lines from the voice.txt file.
Create a directory (audio_text_pairs) to save audio-text pairs.
Initialize recording variables: sample rate (fs) and recording duration (seconds).
Define a function record_fn(action) that handles recording, playback, and saving of audio files based on the user's action. This function also skips phrases that have already been recorded and saved. If all phrases have been recorded, it will display a completion message.
Finally, it launches a Gradio interface (iface) that connects the record function (record_fn) to the interface's actions (Start Recording, Stop Recording, Play Recording, Save Recording).
## audio-cleaner.py

This script uses the pydub library to process audio files in the audio_text_pairs directory. It removes silence from each .wav file and overwrites the original file with the trimmed version.

Here's a detailed walkthrough:

Import necessary libraries - pydub.AudioSegment, pydub.silence.detect_nonsilent, functools.reduce, and os.
Define a function trim_silence(audio) that detects non-silent parts of an audio and trims the silent parts.
Iterate over all .wav files in the audio_text_pairs directory, and for each file, it trims the silent parts and overwrites the original file with the trimmed version.
