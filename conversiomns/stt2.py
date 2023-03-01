import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write, read

def text_to_frequency(text):
    # Convert the text to lowercase and remove non-alphabetic characters
    text = ''.join(filter(str.isalpha, text.lower()))

    # Convert the text to a sequence of ASCII codes
    ascii_codes = np.array([ord(c) for c in text])

    # Generate a frequency sequence based on the ASCII codes
    frequencies = np.sin(2 * np.pi * ascii_codes / 128)

    return frequencies

def frequency_to_text(frequencies):
    # Convert the frequencies to a sequence of ASCII codes
    ascii_codes = np.round(128 * np.arcsin(frequencies) / (2 * np.pi)).astype(int)

    # Convert the ASCII codes to text
    text = ''.join([chr(c) for c in ascii_codes])

    return text

# Example usage
text = "Hello, world!"
frequencies = text_to_frequency(text)

# Write the frequency sequence to a .WAV file
sample_rate = 44100
write("output.wav", sample_rate, frequencies)

# Read the frequency sequence from the .WAV file
_, frequencies = read("output.wav")

# Convert the frequency sequence back to text
text_reconstructed = frequency_to_text(frequencies)

print("Original text:", text)
print("Reconstructed text:", text_reconstructed)
