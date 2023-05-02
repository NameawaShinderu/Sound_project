import numpy as np
import sounddevice as sd
from scipy.io import wavfile

# Define the mapping from characters to pitch changes
char_pitch = {
    '0': 0,
    '1': 100,
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
duration = 0.01

# Compute the number of samples for each character
n_samples = int(fs * duration)

# Compute the corresponding pitch changes
pitch_changes = []
for i in range(0, len(waveform), n_samples):
    segment = waveform[i:i+n_samples]
    autocorr = np.correlate(segment, segment, mode='full')
    autocorr = autocorr[len(autocorr)//2:]
    freqs = np.fft.rfftfreq(len(segment), 1/fs)
    spectrum = np.abs(np.fft.rfft(segment))
    pitch_idx = np.argmax(spectrum[(freqs >= 80) & (freqs <= 300)])
    pitch = freqs[(freqs >= 80) & (freqs <= 300)][pitch_idx]
    pitch_change = pitch - char_pitch['0']
    pitch_changes.append(pitch_change)

# Recover the original text
recovered_text = ''
for pitch_change in pitch_changes:
    char = None
    for c, p in char_pitch.items():
        if abs(pitch_change - p) < 10:
            char = c
            break
    if char:
        recovered_text += char
    else:
        recovered_text += '0'

recovered_bin = recovered_text
# Print the original and recovered text
print("Recovered text: ", recovered_bin)

# convert binary string to bytes
def binary_to_bytes(binary_str):
    return int(binary_str, 2).to_bytes(len(binary_str) // 8, byteorder='big')

# concatenate magic bytes for JPEG
magic_bytes = b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01'
image_data = magic_bytes + binary_to_bytes(recovered_bin)
print(image_data)

# write bytes to file
with open('output.jpg', 'wb') as f:
    f.write(image_data)