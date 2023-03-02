import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile

# Define the sampling rate and duration
fs = 44100
duration = 1

# Define the text to be converted into audio
text = input("enter the text:")

# Define the frequencies corresponding to the characters in the text
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

# Convert the text into a sequence of frequencies
# for c in text:
#     print(char_freq[c])


freq_seq = [char_freq[char] for char in text]
print(freq_seq)

# # Generate the sound wave by concatenating sine waves of the specified frequencies
# t = np.linspace(0, duration, fs * duration, False)
# waveform = np.concatenate([np.sin(2 * np.pi * f * t) for f in freq_seq])

# # Save the audio as a .wav file
# wavfile.write('output.wav', fs, waveform)





