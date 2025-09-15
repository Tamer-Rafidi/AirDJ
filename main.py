from audio.audio_player import start_audio_stream
from vision.hand_tracker import HandTracker
from vision.ui_overlay import draw_ui
import cv2
import threading

# Global control flag
is_playing = True


def main():
    """
      Main program loop:
      - Starts audio streaming in a separate thread
      - Captures video from webcam
      - Tracks hand gestures
      - Updates audio parameters in real-time
      - Draws UI overlays
      """
    global is_playing

    # Start audio in a separate thread
    audio_thread = threading.Thread(target=start_audio_stream)
    audio_thread.start()

    # Initialize camera and hand tracker
    cap = cv2.VideoCapture(0)
    hand_tracker = HandTracker()

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frame, hands_data = hand_tracker.process(frame)

            # Draw UI overlays
            draw_ui(frame, hands_data)

            cv2.imshow("Hand-Controlled Audio Effects", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    finally:
        is_playing = False
        audio_thread.join()
        cap.release()
        cv2.destroyAllWindows()
        hand_tracker.close()


if __name__ == "__main__":
    main()
