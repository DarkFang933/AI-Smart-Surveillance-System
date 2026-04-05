import cv2
from ultralytics import YOLO

class PersonDetector:
    def __init__(self):
        # Load YOLOv8 nano model (fastest, good enough for student project)
        self.model = YOLO('yolov8n.pt')

    def detect(self, frame):
        # Run detection — only people (class 0), lower resolution for speed
        results = self.model(frame, classes=0, verbose=False, imgsz=480)

        # Extract bounding boxes
        boxes = []
        for box in results[0].boxes.xyxy:
            boxes.append([int(b) for b in box.tolist()])

        # Draw boxes on frame ourselves (faster than results.plot())
        for (x1, y1, x2, y2) in boxes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        return boxes, frame
