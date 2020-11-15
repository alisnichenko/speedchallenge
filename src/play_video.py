import cv2
import numpy as np
import sys

# Plays video. VLC was drunk today.
def play_video(video_path : str) -> None:
    cap = cv2.VideoCapture(video_path) 
    if not cap.isOpened():
        print('Error opening video file.')
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0XFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    video_path = sys.argv[1]
    print('Opening', video_path)
    print('Press q to quit.')
    play_video(video_path)
