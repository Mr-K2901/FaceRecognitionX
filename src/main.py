# Entry point
import cv2
from core.video_source import LaptopCamera, adjust_gamma, apply_clahe


def main():
    camera = LaptopCamera(camera_index=0)
    camera.start()


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
            frame = adjust_gamma(frame, gamma=1.5)
            frame = apply_clahe(frame, clip_limit=2.0, grid_size=(8, 8))

            if frame is None:
                continue

            cv2.imshow("FaceRecognitionX - Laptop Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.stop()
        cv2.destroyAllWindows()
        print("Camera stopped. Exiting program.")

if __name__ == "__main__":
    main()
