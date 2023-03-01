import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write, read
import matplotlib.pyplot as plt
import soundfile as sf

text = input("enter the text:")
slices = list(text)

print(slices)

A = []
for num in slices:
    av = ord(num)
    A.append(av)
   
print(A)
# input numerical data

# apply Fourier transform to get frequency spectrum
freq_spectrum = np.fft.fft(A)

# get the corresponding frequencies
freq = np.fft.fftfreq(len(A))
print(freq)

# get the corresponding frequencies in Hz
sampling_rate = 44100
freq_hz = freq * sampling_rate
plt.plot(freq_hz, abs(freq_spectrum))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

time_waveform = np.fft.ifft(freq_spectrum)
sf.write('test.wav', time_waveform.real, sampling_rate)


#for slice in slices:
    #av = ord(text)
    #print(av)    



