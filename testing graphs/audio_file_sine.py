import numpy as np
import soundfile as sf

# set parameters
duration = 5  # seconds
sampling_rate = 44100  # Hz
frequency = 440  # Hz

# generate sine wave
time_array = np.linspace(0, duration, duration * sampling_rate, endpoint=False)
waveform = np.sin(2 * np.pi * frequency * time_array)

# apply Fourier transform to get frequency spectrum
freq_spectrum = np.fft.fft(waveform)

# apply inverse Fourier transform to get time-domain waveform
time_waveform = np.fft.ifft(freq_spectrum)

# write waveform to audio file
sf.write('test.wav', time_waveform.real, sampling_rate)
