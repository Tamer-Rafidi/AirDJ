
def get_pixel_coords(landmark, frame_shape):
    h, w, _ = frame_shape
    return int(landmark.x * w), int(landmark.y * h)
