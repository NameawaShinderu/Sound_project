import numpy as np
import matplotlib.pyplot as plt

# input numerical data
data = [2, 4, 6, 8, 10, 8, 6, 4]

# apply Fourier transform to get frequency spectrum
freq_spectrum = np.fft.fft(data)

# get the corresponding frequencies
freq = np.fft.fftfreq(len(data))
print(freq)

# get the corresponding frequencies in Hz
sampling_rate = 1000
freq_hz = freq * sampling_rate
plt.plot(freq_hz, abs(freq_spectrum))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()