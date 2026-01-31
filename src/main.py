# Entry point
import cv2
from core.video_source import LaptopCamera

def main():
    camera = LaptopCamera(camera_index=0)
    camera.start()

    try:
        while True:
            frame = camera.read()
            if frame is None:
                continue

            cv2.imshow("FaceRecognitionX - Laptop Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
