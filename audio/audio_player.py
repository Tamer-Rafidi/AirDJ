import numpy as np
import sounddevice as sd
import soundfile as sf
from scipy.signal import butter, lfilter, lfilter_zi
import threading
from config.constants import AUDIO_FILE, AUDIO_STATE

# Load audio
AUDIO_STATE['data'], AUDIO_STATE['samplerate'] = sf.read(AUDIO_FILE, dtype='float32')
nyquist = AUDIO_STATE['samplerate'] / 2

# Filter setup
def update_filter_coefficients(cutoff):
    """
    Compute Butterworth low-pass filter coefficients based on cutoff frequency
    Ensures cutoff is within [100 Hz, nyquist - 100 Hz]
    """
    cutoff = max(100, min(nyquist - 100, cutoff))
    b, a = butter(1, cutoff / nyquist, btype='low', analog=False)
    return b, a


def audio_callback(outdata, frames, status):
    """
    This callback is called by sounddevice for every audio buffer.
    - Applies volume and low-pass filter
    - Adjusts playback speed by advancing play_index
    """
    if status:
        print(status)

    data = AUDIO_STATE['data']
    output = np.zeros((frames, 2), dtype=np.float32)

    with AUDIO_STATE['lock']:
        b, a = update_filter_coefficients(AUDIO_STATE['cutoff'])

        for i in range(frames):
            idx = int(AUDIO_STATE['play_index'])
            if idx >= len(data):
                AUDIO_STATE['play_index'] = 0
                idx = 0
            output[i] = data[idx]
            AUDIO_STATE['play_index'] += AUDIO_STATE['speed']

        if AUDIO_STATE['zi'] is None:
            zi = lfilter_zi(b, a)
            AUDIO_STATE['zi'] = np.tile(zi[:, np.newaxis], (1, 2))

        filtered, AUDIO_STATE['zi'] = lfilter(b, a, output, axis=0, zi=AUDIO_STATE['zi'])
        outdata[:] = filtered * AUDIO_STATE['volume']


def start_audio_stream():
    AUDIO_STATE['play_index'] = 0.0
    with sd.OutputStream(callback=audio_callback, samplerate=AUDIO_STATE['samplerate'], channels=2):
        while AUDIO_STATE['running']:
            sd.sleep(100)
