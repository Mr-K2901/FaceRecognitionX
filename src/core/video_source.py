# Webcam / ESP32 abstraction
import cv2

#-----------------------------------------------------------------------------------------------------------
# Laptop Camera
#-----------------------------------------------------------------------------------------------------------

class LaptopCamera:
    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index
        self.cap = None

    def start(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise RuntimeError("Could not open laptop camera")

    def read(self):
        if self.cap is None:
            return None
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def stop(self):
        if self.cap:
            self.cap.release()
