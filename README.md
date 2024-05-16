# MultiCameraArray

**MultiCameraArray** is an IoT project designed to capture images from multiple ESP32-CAM modules and send them to a central Flask server for storage and display. This setup can be used for applications such as surveillance, 3D reconstruction, or environmental monitoring.

## Features

- **Multiple Camera Integration**: Uses multiple ESP32-CAM modules to capture images.
- **Wireless Data Transmission**: Utilizes the ESP32-CAM’s Wi-Fi capabilities to send images to a remote server.
- **Flask Server**: Implements a Flask server to receive, process, and display the images.
- **Real-Time Data Visualization**: Displays the captured images on a web interface.

## Components

- **ESP32-CAM Modules**
- **Power Supply (e.g., USB cables or battery packs for each ESP32-CAM)**
- **Wi-Fi Network**
- **Central Server (e.g., Raspberry Pi or any server running Flask)**
- **Cables and Connectors**

## Setup

### ESP32-CAM Nodes

1. **Flash MicroPython firmware to your ESP32-CAM.**
2. **Upload `camera_main.py` to your ESP32-CAM using a tool like `ampy` or `mpfshell`.**
   ```bash
   ampy --port /dev/ttyUSB0 put camera_main.py
