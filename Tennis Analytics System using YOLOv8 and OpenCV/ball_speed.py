from ultralytics import YOLO
import cv2
import math

# Load YOLO model
model = YOLO("yolov8n.pt")

# Input video
video_path = "input_video/input_video.mp4"

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "ball_speed_output.mp4",
    fourcc,
    fps,
    (width, height)
)

prev_center = None

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, verbose=False)

    for box in results[0].boxes:

        cls = int(box.cls[0])

        # COCO sports ball class
        if cls == 32:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            if prev_center is not None:

                pixel_distance = math.sqrt(
                    (cx - prev_center[0]) ** 2 +
                    (cy - prev_center[1]) ** 2
                )

                # Rough conversion
                pixels_per_meter = 100

                distance_meters = pixel_distance / pixels_per_meter

                speed_mps = distance_meters * fps
                speed_kmh = speed_mps * 3.6

                cv2.putText(
                    frame,
                    f"Speed: {speed_kmh:.1f} km/h",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                print(f"Speed: {speed_kmh:.1f} km/h")

            prev_center = (cx, cy)

    out.write(frame)

cap.release()
out.release()

print("Done!")
print("Saved as: ball_speed_output.mp4")