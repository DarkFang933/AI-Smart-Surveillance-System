import cv2

def draw_overlay(frame, people_count, suspicious):
    """Draw the HUD overlay on the frame."""
    h, w = frame.shape[:2]

    # --- Top-left info panel (semi-transparent dark background) ---
    overlay = frame.copy()
    panel_h = 130 if not suspicious else 170
    cv2.rectangle(overlay, (10, 10), (420, panel_h), (30, 30, 30), -1)
    cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)

    # Title
    cv2.putText(frame, "AI Smart Surveillance System",
                (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 200), 2)

    # Status
    cv2.putText(frame, "Status: Monitoring",
                (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

    # People count
    cv2.putText(frame, f"People Count: {people_count}",
                (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

    # Suspicious activity warning
    if suspicious:
        cv2.putText(frame, "!! Suspicious Activity Detected",
                    (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

    return frame
