import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write, read
import matplotlib.pyplot as plt
import soundfile as sf

text = input("enter the text:")
text = text.lower().replace(" ", "")

#slices = list(text)

#print(slices)

av = [ord(num)for num in text]
print(av)
# A = []
# for num in text:
#     av = ord(num)
#     A.append(av)
    # print(av)
   
#print(A)
# input numerical data

# apply Fourier transform to get frequency spectrum
freq_spectrum = np.fft.fft(av)

# get the corresponding frequencies
freq = np.fft.fftfreq(len(av))
print(freq)


# # get the corresponding frequencies in Hz
sampling_rate = 44100
duration = 1
freq_hz = freq * sampling_rate
plt.plot(freq_hz, abs(freq_spectrum))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

# #concatenate the frequencies to the
t = np.linspace(0, duration, sampling_rate * duration, False)
waveform = np.concatenate([np.sin(2 * np.pi * f * t) for f in av])

sf.write('mycode.wav',waveform, sampling_rate)


# time_waveform = np.fft.ifft(freq_spectrum)
 #sf.write('mycode.wav', waveform, sampling_rate)




#for slice in slices:
    #av = ord(text)
    #print(av)    



