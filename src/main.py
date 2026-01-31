import cv2
from core.video_source import LaptopCamera, adjust_gamma, apply_clahe
from core.detector import FaceDetector

def main():
    camera = LaptopCamera(camera_index=0)
    camera.start()

    CASCADE_PATH = "assets/haarcascade_frontalface_default.xml"
    detector = FaceDetector(CASCADE_PATH)


    cv2.namedWindow(
        "FaceRecognitionX - Laptop Camera",
        cv2.WINDOW_NORMAL
    )

    cv2.setWindowProperty(
        "FaceRecognitionX - Laptop Camera",
        cv2.WND_PROP_FULLSCREEN,
        cv2.WINDOW_FULLSCREEN
    )


    try:
        while True:
            #frame = camera.read()
            frame = camera.read()
            

            if frame is None:
                continue
            frame = adjust_gamma(frame, gamma=1.5)
            frame = apply_clahe(frame, clip_limit=2.0, grid_size=(8, 8))

            faces = detector.detect(frame)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("FaceRecognitionX - Laptop Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.stop()
        cv2.destroyAllWindows()
        print("Camera stopped. Exiting program.")

if __name__ == "__main__":
    main()
