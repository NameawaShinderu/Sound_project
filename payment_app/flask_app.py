import numpy as np
import sounddevice as sd
from scipy.io import wavfile
import scipy.fftpack as fft

from flask import Flask, render_template, redirect, url_for, Response
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
Bootstrap(app)

# Define the mapping from characters to frequencies
char_freq = {
    '0': 1000,
    '1': 1500,
    '2': 2000,
    '3': 2500,
    '4': 3000,
    '5': 3500,
    '6': 4000,
    '7': 4500,
    '8': 5000,
    '9': 5500
}

class RecordForm(FlaskForm):
    record = SubmitField('Record')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RecordForm()
    if form.validate_on_submit():
        return redirect(url_for('record'))
    return render_template('index.html', form=form)

@app.route('/record')
def record():
    duration = 12
    fs = 44100
    n_samples = int(fs * duration)
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    waveform = recording.flatten()
    wavfile.write('output.wav', fs, waveform)

    return redirect(url_for('playback'))

@app.route('/playback')
def playback():
    # Load the audio file
    fs, waveform = wavfile.read('output.wav')

    # Compute the duration of each character in seconds
    duration = 1

    # Compute the number of samples for each character
    n_samples = int(fs * duration)

    # Compute the corresponding frequencies
    freqs = fft.fftfreq(n_samples) * fs

    # Recover the original text
    recovered_text = ''
    for i in range(0, len(waveform), n_samples):
        segment = waveform[i:i+n_samples]
        freq_spectrum = fft.fft(segment)
        freq_index = np.argmax(np.abs(freq_spectrum))
        freq = freqs[freq_index]
        char = None
        for c, f in char_freq.items():
            if abs(freq - f) < 10:
                char = c
                break
        print(i)
        print(c)
        if char:
            recovered_text += char
        else:
            recovered_text += '?'

    # Print the original and recovered text
    print("Recovered text: ", recovered_text)

    def generate():
        with open("output.wav", "rb") as f:
            data = f.read(1024)
            while data:
                yield data
                data = f.read(1024)

    return Response(generate(), mimetype="audio/x-wav")

if __name__ == '__main__':
    app.run(debug=True)
