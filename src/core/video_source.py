# Webcam / ESP32 abstraction
import cv2

#-----------------------------------------------------------------------------------------------------------
# CLAHE / Adjust Gamma
#-----------------------------------------------------------------------------------------------------------

import numpy as np
def adjust_gamma(image, gamma=1.4):
    inv_gamma = 1.0 / gamma
    table = np.array(
        [((i / 255.0) ** inv_gamma) * 255 for i in range(256)]
    ).astype("uint8")
    return cv2.LUT(image, table)

def apply_clahe(image, clip_limit=2.0, grid_size=(8, 8)):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(
        clipLimit=clip_limit,
        tileGridSize=grid_size
    )
    l = clahe.apply(l)

    lab = cv2.merge((l, a, b))
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

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
