import numpy as np
import scipy.fftpack as fft
from scipy.io import wavfile

# Load the audio file
fs, waveform = wavfile.read('output.wav')

# Compute the frequency spectrum of the audio waveform
freq_spectrum = fft.fft(waveform)

# Compute the corresponding frequencies
freqs = fft.fftfreq(len(waveform)) * fs
print(freqs)

# Identify the frequencies corresponding to 'h' and 'i'
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

h_freq = char_freq['h']
i_freq = char_freq['i']

# Find the indices of the frequency spectrum corresponding to 'h' and 'i'
h_index = np.argmin(np.abs(freqs - h_freq))
i_index = np.argmin(np.abs(freqs - i_freq))

# Check which of the frequencies has a higher amplitude in the spectrum
if abs(freq_spectrum[h_index]) > abs(freq_spectrum[i_index]):
    text = 'h'
else:
    text = 'i'

# Print the recovered text
print(text)
