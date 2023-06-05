import gradio as gr
import sounddevice as sd
import soundfile as sf
import numpy as np
import os

# Read lines from the voices.txt file
with open('voice.txt', 'r') as f:
    phrases = f.read().splitlines()

# Create a directory to save your files
if not os.path.exists('audio_text_pairs'):
    os.makedirs('audio_text_pairs')

# Initialize recording variables
fs = 44100  # Sample rate
seconds = 10  # Duration of recording
recording = np.zeros((fs*seconds,))  # Initialize array to hold recording

# Initialize phrase index
current_phrase_idx = 0

def record_fn(action):
    global recording, current_phrase_idx

    # Skip to the next phrase if the audio-text pair already exists
    while os.path.exists(f'audio_text_pairs/{current_phrase_idx}.wav') and os.path.exists(f'audio_text_pairs/{current_phrase_idx}.txt'):
        current_phrase_idx += 1
        # Check if all phrases have been recorded
        if current_phrase_idx >= len(phrases):
            return "All phrases have been recorded."

    if action == "Start Recording":
        # Start recording for the specified duration
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    elif action == "Stop Recording":
        # Stop the recording
        sd.stop()
    elif action == "Play Recording":
        # Play back the current recording
        sd.play(recording, fs)
    elif action == "Save Recording":
        # Save the recording
        audio_filename = f'audio_text_pairs/{current_phrase_idx}.wav'
        text_filename = f'audio_text_pairs/{current_phrase_idx}.txt'
    
        # Save audio file
        sf.write(audio_filename, recording, fs)
    
        # Save corresponding text to a file
        with open(text_filename, 'w') as file:
            file.write(phrases[current_phrase_idx])

        # Move to the next phrase
        current_phrase_idx += 1

        # Check if all phrases have been recorded
        if current_phrase_idx >= len(phrases):
            return "Recording saved successfully. All phrases have been recorded."

        return "Recording saved successfully. Next phrase: " + phrases[current_phrase_idx]

    # Return current phrase to display
    return "## Recording saved successfully. Next phrase: " + phrases[current_phrase_idx]

iface = gr.Interface(
    fn=record_fn, 
    inputs=[
        gr.Radio(["Start Recording", "Stop Recording", "Play Recording", "Save Recording"], label="Actions"),
    ], 
    outputs="text",
    title="ATLAS VOICE Recording Interface",
    description="Please record the given phrase and save it.",
)

iface.launch(inbrowser=bool)
