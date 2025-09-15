import cv2
from config.constants import BLUE_COLOR, LIGHT_ORANGE, AUDIO_STATE

def draw_ui(frame, hands_data):
    height, _ = frame.shape[:2]

    # Right hand (volume and cutoff)
    if 'wrist_px' in hands_data['right']:
        wrist = hands_data['right']['wrist_px']
        radius = int(10 + AUDIO_STATE['volume'] * 10)
        cv2.line(frame, wrist, (wrist[0], height - 1), BLUE_COLOR, 3)
        cv2.circle(frame, (wrist[0], height - 10), radius, BLUE_COLOR, -1)
        cv2.putText(frame, f'Vol: {AUDIO_STATE["volume"]:.2f}', (wrist[0] - 120, wrist[1] + 30),
                    cv2.FONT_HERSHEY_DUPLEX, 0.65, BLUE_COLOR, 2)

    if 'thumb_px' in hands_data['right'] and 'index_px' in hands_data['right']:
        thumb = hands_data['right']['thumb_px']
        index = hands_data['right']['index_px']
        cv2.line(frame, thumb, index, BLUE_COLOR, 4)
        mid_x = (thumb[0] + index[0]) // 2
        mid_y = (thumb[1] + index[1]) // 2
        cv2.putText(frame, f'{int(AUDIO_STATE["cutoff"])} Hz', (mid_x - 100, mid_y),
                    cv2.FONT_HERSHEY_DUPLEX, 0.65, BLUE_COLOR, 2)

    # Left hand (playback speed)
    # if 'wrist_px' in hands_data['left']:
    #     wrist = hands_data['left']['wrist_px']
    #     speed_norm = (AUDIO_STATE['speed'] - 0.75) / (1.25 - 0.75)
    #     radius = int(10 + speed_norm * 10)
    #     cv2.line(frame, wrist, (wrist[0], height - 1), LIGHT_ORANGE, 3)
    #     cv2.circle(frame, (wrist[0], height - 10), radius, LIGHT_ORANGE, -1)
    #     cv2.putText(frame, f'Speed: {AUDIO_STATE["speed"]:.2f}x', (wrist[0] + 20, wrist[1] + 20),
    #                 cv2.FONT_HERSHEY_DUPLEX, 0.65, LIGHT_ORANGE, 2)

    if 'thumb_px' in hands_data['left'] and 'index_px' in hands_data['left']:
        thumb = hands_data['left']['thumb_px']
        index = hands_data['left']['index_px']
        cv2.line(frame, thumb, index, LIGHT_ORANGE, 4)
        mid_x = (thumb[0] + index[0]) // 2
        mid_y = (thumb[1] + index[1]) // 2
        cv2.putText(frame, f'{AUDIO_STATE["speed"]:.2f}x', (mid_x + 10, mid_y),
                    cv2.FONT_HERSHEY_DUPLEX, 0.65, LIGHT_ORANGE, 2)
