from ultralytics import YOLO
import cv2

# Load model
model = YOLO("models/yolov8n.pt")

# Input video
video_path = "input_video/input_video.mp4"

# Tracking
results = model.track(
    source=video_path,
    tracker="bytetrack.yaml",
    conf=0.25,
    save=True,
    persist=True
)

print("Tracking Completed")