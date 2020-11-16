"""
Contains necessary methods and functions that are not related to the
network directly, but complete clerical tasks, such as frame collection,
lookups, synchronization, etc.
"""
import cv2
import numpy as np

def get_frames_list(video_path: str) -> np.array:
    """
    Retrieves the list of frames made from video. The list of images will be
    of type np.array for ease of model training, labeling, modification, etc.
    Args:
        video_path: string that contains the path to desired video.
    Returns:
        A numpy array created from a Python list storing given video frames.
    """
    frames = []
    # Gets video handle.
    cap = cv2.VideoCapture(video_path)
    # Throws an exception if the video opening failed.
    if not cap.isOpened():
        raise FileNotFoundError(video_path, "File not found.")
    # Reads the first frame.
    flag, frame = cap.read()
    # While reads properly.
    while flag:
        # Shows the image.
        cv2.imshow('video', frame)
        flag, frame = cap.read()
        # Switches flag if 'q' pressed on the keyboard.
        if cv2.waitKey(25) & 0XFF == ord('q'):
            flag = False
    # Cleans up.
    cap.release()
    cv2.destroyAllWindows()
    # Return np.array
    return np.array(frames)
