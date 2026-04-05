import cv2

class AlertSystem:
    def __init__(self):
        # Color for the alert text (red in BGR)
        self.text_color = (0, 0, 255)
        
    def send_alerts(self, alerts, frame):
        # Print each alert to the terminal
        for alert in alerts:
            print("ALERT:", alert)
            
        # Draw each alert on the frame
        y_position = 40
        for alert in alerts:
            cv2.putText(frame, alert, (10, y_position), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, self.text_color, 2)
            y_position += 35
            
        return frame
