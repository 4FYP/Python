# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vEKai_O9_tRUh3NIHJrcuDDRdwAJjo_B
"""

from google.colab import drive
drive.mount('/content/drive')

pip install ultralytics

pip install numpy opencv-python torch torchvision torchaudio

from ultralytics import YOLO
import cv2
model = YOLO('yolov8n.pt')

results=model('/content/1.png')
for result in results:
  annotated_frame=result.plot()
  cv2.imwrite('output_img.jpg', annotated_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open video file
video_path = "/content/VID-20250315-WA0000.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"this is {fps}")
# Define video writer to save output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
out = cv2.VideoWriter("output_video.mp4", fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Stop if video ends

    # Run YOLOv8 detection
    results = model(frame)

    # Get the annotated frame (in RGB) and convert back to BGR
    annotated_frame = results[0].plot()
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

    # Save frame to output video
    out.write(annotated_frame)

# Release resources
cap.release()
out.release()

print("✅ Video saved as output_video.mp4 🎥")

for r in results:
  annotated_frames=r.plot()
  cv2.VideoWriter()

fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the video writer to save output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
out = cv2.VideoWriter("output_video.mp4", fourcc, fps, (width, height))

