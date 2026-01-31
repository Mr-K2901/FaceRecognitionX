# FaceRecognitionX

A robust, dual-mode face recognition pipeline designed for IoT environments. It enables real-time identification using either a local webcam or a networked ESP32-CAM stream, featuring automatic failover and local data logging.

![Project Status](https://img.shields.io/badge/status-active-brightgreen) ![Python](https://img.shields.io/badge/python-3.10-blue)


Python-based face recognition system that works with:
- Laptop webcam
- ESP32-CAM (as IP camera)

All processing (video decoding, face detection, recognition, logging) runs on the client machine.

---

## What it does

- Reads live video from laptop camera (current phase)
- (Later) Reads MJPEG stream from ESP32-CAM
- Processes frames using OpenCV
- (Later) Detects and recognizes faces
- Logs results locally

---

## How to run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
