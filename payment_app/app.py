import numpy as np
import scipy.fftpack as fft
from scipy.io import wavfile
import pyaudio

# Define the mapping from characters to frequencies
char_freq = {
    '0': 1000,
    '1': 1500,
    '2': 2000,
    '3': 2500,
    '4': 3000,
    '5': 3500,
    '6': 4000,
    '7': 4500,
    '8': 5000,
    '9': 5500
}

# Get the text to convert to audio
text = input("Enter text to convert to audio: ")

# Convert the text to lowercase and remove whitespace
text = text.lower().replace(" ", "")

# Compute the duration of each character in seconds
duration = 0.5

# Compute the sampling rate and the number of samples for each character
fs = 44100
n_samples = int(fs * duration)

# Create an empty waveform for the audio
waveform = np.zeros(n_samples * len(text))

# Generate the audio waveform
for i, char in enumerate(text):
    freq = char_freq[char]
    t = np.arange(n_samples) / fs
    waveform[i * n_samples:(i + 1) * n_samples] = 0.5 * np.sin(2 * np.pi * freq * t)

# Scale the waveform to the range [-1, 1]
max_val = np.max(np.abs(waveform))
waveform /= max_val

# Save the waveform to a WAV file
wavfile.write('output.wav', fs, waveform)

# Play the audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
stream.write(waveform.astype(np.float32).tobytes())
stream.stop_stream()
stream.close()
p.terminate()
