
import threading

# Audio path
AUDIO_FILE = '' #Path to song you want to play around with

# UI colors (BGR)
BLUE_COLOR = (255, 0, 0)
LIGHT_ORANGE = (50, 180, 255)

# Shared state for audio parameters
AUDIO_STATE = {
    'volume': 1.0,
    'cutoff': 1000.0,
    'speed': 1.0,
    'play_index': 0.0,
    'zi': None,
    'running': True,
    'lock': threading.Lock()
}
