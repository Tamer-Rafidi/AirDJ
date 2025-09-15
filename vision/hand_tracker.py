import mediapipe as mp
import cv2
import numpy as np
from utils.helpers import get_pixel_coords
from config.constants import AUDIO_STATE

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

class HandTracker:
    def __init__(self):
        self.hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

    def process(self, frame):
        height, width, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        hands_data = {
            'right': {},
            'left': {},
        }

        if results.multi_hand_landmarks and results.multi_handedness:
            for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                label = results.multi_handedness[i].classification[0].label
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if label == 'Right':
                    wrist = hand_landmarks.landmark[0]
                    thumb = hand_landmarks.landmark[4]
                    index = hand_landmarks.landmark[8]

                    AUDIO_STATE['volume'] = np.clip(1.0 - wrist.y, 0.0, 1.0)
                    dist = np.linalg.norm([thumb.x - index.x, thumb.y - index.y])
                    AUDIO_STATE['cutoff'] = np.interp(dist, [0.02, 0.15], [200, 1000])

                    hands_data['right']['wrist_px'] = get_pixel_coords(wrist, frame.shape)
                    hands_data['right']['thumb_px'] = get_pixel_coords(thumb, frame.shape)
                    hands_data['right']['index_px'] = get_pixel_coords(index, frame.shape)

                elif label == 'Left':
                    thumb = hand_landmarks.landmark[4]
                    index = hand_landmarks.landmark[8]
                    dist = np.linalg.norm([thumb.x - index.x, thumb.y - index.y])
                    AUDIO_STATE['speed'] = np.interp(dist, [0.02, 0.15], [0.75, 1.25])

                    hands_data['left']['thumb_px'] = get_pixel_coords(thumb, frame.shape)
                    hands_data['left']['index_px'] = get_pixel_coords(index, frame.shape)
                    hands_data['left']['wrist_px'] = get_pixel_coords(hand_landmarks.landmark[0], frame.shape)

        return frame, hands_data

    def close(self):
        self.hands.close()
