import numpy as np
import sounddevice as sd
from scipy.io import wavfile
import scipy.fftpack as fft

# Define the mapping from characters to frequencies
char_freq = {
    'a': 440,
    'b': 494,
    'c': 523,
    'd': 587,
    'e': 659,
    'f': 698,
    'g': 784,
    'h': 880,
    'i': 988,
    'j': 1047,
    'k': 1175,
    'l': 1319,
    'm': 1397,
    'n': 1568,
    'o': 1760,
    'p': 1976,
    'q': 2093,
    'r': 2349,
    's': 2637,
    't': 2794,
    'u': 3136,
    'v': 3520,
    'w': 3951,
    'x': 4186,
    'y': 4699,
    'z': 5274
    
}

# Record and write the audio file
duration = 12
fs = 44100
n_samples = int(fs * duration)
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
waveform = recording.flatten()
wavfile.write('tmp.wav', fs, waveform) 

# Load the audio file
fs, waveform = wavfile.read('tmp.wav')

# Compute the duration of each character in seconds
duration = 1

# Compute the number of samples for each character
n_samples = int(fs * duration)

# Compute the corresponding frequencies
freqs = fft.fftfreq(n_samples) * fs

# Recover the original text
recovered_text = ''
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
        recovered_text += '?'

# Print the original and recovered text
print("Recovered text: ", recovered_text)
