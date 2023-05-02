import numpy as np
import sounddevice as sd
from scipy.io import wavfile
import scipy.fftpack as fft
import binascii

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
    '9': 5500,
    'a': 6000,
    'b': 6500,
    'c': 7000,
    'd': 7500,
    'e': 8000,
    'f': 8500,
}

# Record and write the audio file
duration = 1
fs = 44100
n_samples = int(fs * duration)
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
waveform = recording.flatten()
wavfile.write('tmp.wav', fs, waveform)

# Load the audio file
fs, waveform = wavfile.read('output.wav')

# Compute the duration of each character in seconds
duration = 0.1

# Compute the number of samples for each character
n_samples = int(fs * duration)

# Compute the corresponding frequencies
freqs = fft.fftfreq(n_samples) * fs

# Recover the original text
recovered_text = 'FFD8FFE000104A4649460001'
for i in range(0, len(waveform), n_samples):
    segment = waveform[i:i+n_samples]
    freq_spectrum = fft.fft(segment)
    freq_index = np.argmax(np.abs(freq_spectrum))
    freq = freqs[freq_index]
    char = None
    for c, f in char_freq.items():
        if abs(freq - f) < 10:
            char = c
            break
    print(i)
    print(c)
    if char:
        recovered_text += char
    else:
        recovered_text += '0'

recovered_hex = recovered_text
# Print the original and recovered text
print("Recovered text: ", recovered_hex)

# convert hex string to bytes
image_data = binascii.unhexlify(recovered_hex)

# write bytes to file
with open('output.jpg', 'wb') as f:
    f.write(image_data)