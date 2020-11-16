"""
File dedicated for testing and evaluation. The actual functions are going
to be determined later in the process. Currently, only testing.
"""
from speedchallenge_utils import get_frames_list

def main() -> None:
    video_path = "../data/train.mp4"
    print("[INFO] driver.py. Running get_frames_list(). Press q to stop...")
    frames = get_frames_list(video_path)

if __name__ == "__main__":
    print("[INFO] driver.py: Running main()...")
    main()
