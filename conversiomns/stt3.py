import numpy as np
from scipy.io.wavfile import read

def frequency_to_text(frequencies):
    # Convert the frequencies to a sequence of ASCII codes
    ascii_codes = np.round(128 * np.arcsin(frequencies) / (2 * np.pi)).astype(int)

    # Convert the ASCII codes to text
    text = ''.join([chr(c) for c in ascii_codes])

    return text

# Read the frequency sequence from the .WAV file
sample_rate, frequencies = read("output.wav")

# Normalize the frequency sequence to between -1 and 1
frequencies = frequencies / np.max(np.abs(frequencies))

# Convert the frequency sequence back to text
text_reconstructed = frequency_to_text(frequencies)

print("Reconstructed text:", text_reconstructed)
