class SuspiciousActivityAnalyzer:
    def __init__(self):
        # Track how long each person stays roughly in the same spot
        self.prev_boxes = []
        self.loiter_count = 0

        # If someone barely moves for this many frames, flag it
        self.loiter_threshold = 50

    def check_activity(self, people_boxes):
        suspicious = False

        # Compare current boxes to previous frame
        if self.prev_boxes and people_boxes:
            for box in people_boxes:
                cx = (box[0] + box[2]) // 2
                cy = (box[1] + box[3]) // 2
                for prev in self.prev_boxes:
                    px = (prev[0] + prev[2]) // 2
                    py = (prev[1] + prev[3]) // 2

                    # If a person hasn't moved much
                    if abs(cx - px) < 30 and abs(cy - py) < 30:
                        self.loiter_count += 1
                        break

        # Reset if nobody is there
        if not people_boxes:
            self.loiter_count = 0

        # Flag as suspicious if loitering too long
        if self.loiter_count > self.loiter_threshold:
            suspicious = True

        # Save current boxes for next frame comparison
        self.prev_boxes = people_boxes

        return suspicious
