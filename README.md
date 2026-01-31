# FaceRecognitionX

A robust, dual-mode face recognition pipeline designed for IoT environments. It enables real-time identification using either a local webcam or a networked ESP32-CAM stream, featuring automatic failover and local data logging.

![Project Status](https://img.shields.io/badge/status-active-brightgreen) ![Python](https://img.shields.io/badge/python-3.10-blue)

## Overview

FaceRecognitionX solves the problem of unstable IoT video feeds by implementing a "client-side processing" architecture. Instead of running heavy ML models on the ESP32, the microcontroller acts as a simple IP camera, while this Python client handles frame decoding, face detection (HOG/CNN), and recognition.

**Key Capabilities:**
* **Dual Source:** Auto-detects ESP32 stream; fails back to Laptop Webcam (Index 0) if unavailable.
* **Zero-Overwrite Logging:** Ensures no data loss by appending timestamps to logs.
* **Configurable Backend:** Centralized `config.py` for managing IP addresses, thresholds, and paths.
* **Privacy-First:** All face encodings and logs are stored locally, not in the cloud.

## Architecture

```mermaid
graph TD
    A[ESP32-CAM] -- MJPEG Stream (WiFi) --> B[Python Client]
    C[Laptop Webcam] -- USB Feed --> B
    B --> D{Face Recognition}
    D -- Match Found --> E[Log to CSV]
    D -- Unknown --> F[Alert/Ignore]