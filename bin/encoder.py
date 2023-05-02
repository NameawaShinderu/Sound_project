import numpy as np
from scipy.io import wavfile
import pyaudio
from PIL import Image

# image to hex conversion
img_path = input("Enter image path:  ")
img = Image.open(img_path)
img = img.convert("L")  # Convert to true-color mode
img.save("comp.jpeg", format="JPEG", optimize=True, subsampling=0, quality=0)

binary_data = ''
with open('comp.jpeg', 'rb') as f:
    binary_data = ''.join(format(byte, '08b') for byte in f.read())    
print(binary_data)

# Define the mapping from characters 
# to frequencies
char_freq = {
    '0': 1000,
    '1': 5000,
}

# Compute the duration of each character in seconds
duration = 0.01

# Compute the sampling rate and the number of samples for each character
fs = 44100
n_samples = int(fs * duration)

# Create an empty waveform for the audio
waveform = np.zeros(n_samples * len(binary_data))

# Generate the audio waveform
for i, char in enumerate(binary_data):
    freq = char_freq[char]
    t = np.arange(n_samples) / fs
    waveform[i * n_samples:(i + 1) * n_samples] = 0.5 * np.sin(2 * np.pi * freq * t)

# Save the waveform to a WAV file
wavfile.write('output.wav', fs, waveform.astype(np.float32))

# Play the audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
stream.write(waveform.astype(np.float32).tobytes())
stream.stop_stream()
stream.close()
p.terminate()