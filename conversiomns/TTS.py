import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf


def text_to_frequency(text):
    # Assign numerical values to each letter of the alphabet
    ascii_values = [ord(c) for c in text.lower()]

    # Apply a sine wave function to the numerical sequence
    frequency_sequence = np.sin(2 * np.pi * np.array(ascii_values) / len(text))

    # Normalize the frequency sequence
    frequency_sequence /= np.max(np.abs(frequency_sequence), axis=0)

    return frequency_sequence


# Example usage
text = "Madar chod teri maa ka chodu tera maa ka bhosda k liye bolta h diliver ho jyega product tera maa ka bhosda phone se contact nhi kr skta randi chinar chodi bhg madar chod tera maa ka chodu amazone ka sab staff ka maa bhen chodu chinal chodi randi ka bacca log haaattt madar chod"
frequency_sequence = text_to_frequency(text)

# Write the frequency sequence to a .WAV file
sample_rate = 44100
write("output.wav", sample_rate, frequency_sequence)
