#  AirDJ – Hand-Tracking Audio Controller

**AirDJ** is a real-time hand-tracking audio controller that lets you manipulate music using intuitive hand gestures. By tracking your hands with a webcam, it enables dynamic control of **volume, playback speed, and filter effects**—all without touching any hardware. Perfect for live performance or interactive music experiments.

##  Features

-  **Gesture-Based Audio Control**  
  Control multiple aspects of audio in real time using simple hand movements.

-  **Volume & Low-Pass Filter (Right Hand)**  
  Raise or lower your right hand to adjust volume
  Pinch thumb and index finger to modify low-pass filter cutoff

-  **Playback Speed (Left Hand)**  
  Pinch thumb and index finger to control speed from slow-motion to fast-forward.

-  **Live Visual Feedback**  
  Webcam feed displays circles, lines, and text overlays for all controlled parameters.

-  **Real-Time Performance**  
  Multithreaded design ensures smooth audio playback, hand tracking, and UI updates simultaneously.

##  Tech Stack
### Audio & Signal Processing:  
**Python** - Core language for audio and gesture logic      
**Sounddevice & Soundfile** - Real-time playback and file I/O          
**SciPy** - Low-pass filter design        
**NumPy** - Efficient numerical operations          
**FFmpeg & Pydub** - Audio decoding, slicing, and mixing             
**Multithreading & Parallel Processing** - Accelerates song analysis and rendering             

### Computer Vision & UI: 
**MediaPipe** - Hand tracking and landmark detection         
**OpenCV** - Webcam capture and live UI overlay          

### Performance:    
**Multithreading** - Audio runs in a separate thread for uninterrupted playback

##  Project Structure

```text
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
├── main.py                   # Orchestrates webcam, hand tracking, audio, and UI
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

```

##  How to Use

1. Clone the repo:
```bash
git clone https://github.com/Tamer-Rafidi/AirDJ.git
cd AirDJ
```
2. Install dependencies:
    Make sure you have Python 3.10+ installed
```bash
pip install -r requirements.txt
```
3. Run the program:
```bash
python main.py
```

⚠️ Make sure your webcam is connected and accessible.

##  Future Improvements

-  Web or desktop GUI for audio selection
-  Track additional gestures for effects like pan, reverb, or stutter
-  Playlist support for continuous live performance

##  Contributing
Contributions are welcome!
1. Fork the repo
2. Create a new branch (git checkout -b feature-name)
3. Commit your changes (git commit -m "Add new feature")
4. Push to your fork (git push origin feature-name)
5. Open a Pull Request

