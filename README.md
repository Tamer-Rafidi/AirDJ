🤚 AirDJ – Hand-Tracking Audio Controller

AirDJ is a real-time hand-tracking audio controller that lets you manipulate music using intuitive hand gestures. By tracking your hands with a webcam, it enables dynamic control of volume, playback speed, and filter effects—all without touching any hardware. Perfect for live performance or interactive music experiments.

🚀 Features

🎶 Gesture-Based Audio Control
Control multiple aspects of audio in real time using simple hand movements.

🔊 Volume & Low-Pass Filter (Right Hand)

Raise or lower your right hand to adjust volume

Pinch thumb and index finger to modify low-pass filter cutoff

⏩ Playback Speed (Left Hand)

Pinch thumb and index finger to control speed from slow-motion to fast-forward

👁️ Live Visual Feedback

Webcam feed displays circles, lines, and text overlays for all controlled parameters

⏱️ Real-Time Performance

Multithreaded design ensures smooth audio playback, hand tracking, and UI updates simultaneously

🚀 Live Demo

🔗 Demo Video
 (replace with link when available)

🛠️ Tech Stack

🔧 Audio & Signal Processing
Python – Core language for audio and gesture logic
Sounddevice & Soundfile – Real-time playback and file I/O
SciPy – Low-pass filter design
NumPy – Efficient numerical operations

💻 Computer Vision & UI
MediaPipe – Hand tracking and landmark detection
OpenCV – Webcam capture and live UI overlay

⚡ Performance
Multithreading – Audio runs in a separate thread for uninterrupted playback

📁 Project Structure
AirDJ/
├── audio/
│   └── audio_player.py       # Audio streaming, filtering, volume & speed control
├── vision/
│   ├── hand_tracker.py       # Hand detection and gesture-to-audio mapping
│   └── ui_overlay.py         # Draws visual feedback on video frames
├── config/
│   └── constants.py          # Audio parameters and UI colors
├── utils/
│   └── helpers.py            # Helper functions (e.g., convert landmarks to pixels)
├── WhatDidIMiss.wav          # Sample audio file for testing
├── main.py                   # Orchestrates webcam, hand tracking, audio, and UI
└── README.md                 # Project documentation

🧪 How to Use

Clone the repo:

git clone https://github.com/your-username/AirDJ.git
cd AirDJ


Install dependencies:

pip install -r requirements.txt


Run the program:

python main.py


Controls:

Right Hand

Volume: raise/lower wrist

Filter Cutoff: thumb ↔ index distance

Left Hand

Playback Speed: thumb ↔ index distance

⚠️ Make sure your webcam is connected and accessible.

🧰 Future Improvements

🌐 Web or desktop GUI for audio selection

🎵 Support for Spotify/YouTube audio streams

🎚️ Manual override for advanced users

🖐️ Track additional gestures for effects like pan, reverb, or stutter

📑 Playlist support for continuous live performance
