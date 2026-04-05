import cv2
from backend.video.video_handler import VideoHandler
from backend.detection.detector import PersonDetector
from backend.analysis.analyzer import SuspiciousActivityAnalyzer
from backend.utils.draw_utils import draw_overlay

# Set up everything
video = VideoHandler("video.mp4")
detector = PersonDetector()
analyzer = SuspiciousActivityAnalyzer()

# Create output video writer
writer = video.create_writer("output_video.mp4")

print("Starting surveillance system... Press 'q' to quit early.")
print(f"Processing {video.total_frames} frames at {video.fps} FPS")

frame_num = 0

while True:
    # Get a frame from the video
    success, frame = video.get_frame()

    # If no more frames, stop
    if not success:
        break

    frame_num += 1

    # Detect people in the frame
    boxes, drawn_frame = detector.detect(frame)

    # Check for suspicious activity
    suspicious = analyzer.check_activity(boxes)

    # Draw the overlay (title, status, count, alerts)
    drawn_frame = draw_overlay(drawn_frame, len(boxes), suspicious)

    # Save frame to output video
    writer.write(drawn_frame)

    # Show live preview
    cv2.imshow("AI Surveillance", drawn_frame)

    # Print progress every 30 frames
    if frame_num % 30 == 0:
        pct = int(frame_num / video.total_frames * 100)
        print(f"  Progress: {pct}% ({frame_num}/{video.total_frames})")

    # Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stopped early by user.")
        break

# Clean up
writer.release()
video.close()
cv2.destroyAllWindows()
print(f"Done! Processed {frame_num} frames. Output saved to output_video.mp4")
