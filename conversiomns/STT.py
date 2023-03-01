import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write, read

def text_to_frequency(text):
    # Assign numerical values to each letter of the alphabet
    ascii_values = [ord(c) for c in text.lower()]
    
    # Apply a sine wave function to the numerical sequence
    frequency_sequence = np.sin(2 * np.pi * np.array(ascii_values) / len(text))
    
    # Normalize the frequency sequence
    frequency_sequence /= np.max(np.abs(frequency_sequence), axis=0)
    
    return frequency_sequence

def frequency_to_text(frequency_sequence, text_length):
    # Apply the inverse sine wave function to the frequency sequence
    ascii_values = np.round((np.arcsin(frequency_sequence) * text_length / (2 * np.pi))).astype(int)
    
    # Convert the numerical sequence back to text
    text = ''.join([chr(v) for v in ascii_values])
    
    return text

# Example usage
text = "Hello"
frequency_sequence = text_to_frequency(text)

# Write the frequency sequence to a .WAV file
sample_rate = 44100
write("output.wav", sample_rate, frequency_sequence)

# Read the frequency sequence from the .WAV file
_, frequency_sequence = read("output.wav")

# Convert the frequency sequence back to text
text_length = len(text)
text_reconstructed = frequency_to_text(frequency_sequence, text_length)

print("Original text:", text)
print("Reconstructed text:", text_reconstructed)
