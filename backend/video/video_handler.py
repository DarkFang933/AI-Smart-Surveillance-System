import cv2

class VideoHandler:
    def __init__(self, path):
        # Open the video file
        self.video = cv2.VideoCapture(path)

        # Get video properties for the output writer
        self.fps = int(self.video.get(cv2.CAP_PROP_FPS))
        self.width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_frame(self):
        # Read one frame from the video
        success, frame = self.video.read()
        return success, frame

    def create_writer(self, output_path):
        # Create a video writer to save output
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_path, fourcc, self.fps, (self.width, self.height))
        return writer

    def close(self):
        # Close the video when done
        self.video.release()
