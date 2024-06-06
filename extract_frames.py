import cv2
import os

# Path to your video file
video_path_list = ["25_04_2021-17h35-19h35.mp4", "28_06_2021-10h32-12h32.mp4"]

def extract_frames(video_path, interval=5):
    # Open video file
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(frame_rate * interval)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            frame = cv2.resize(frame, (1280, 720))
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            video_name = os.path.basename(video_path).split(".")[0]
            cv2.imwrite(f"keyframes/frame_{video_name}_{frame_count}.jpg", frame)
            frames.append(frame)
        frame_count += 1
    cap.release()
    return frames

for video_path in video_path_list:
    # Extract frames from the video at 10-second intervals
    frames = extract_frames(video_path, interval=10)
    os.makedirs("keyframes", exist_ok=True)
    print(f"Extracted {len(frames)} frames from {video_path}")