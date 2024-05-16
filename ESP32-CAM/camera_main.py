import network
import urequests
import time
from machine import Pin
import esp32
import gc

# Replace with your network credentials
SSID = 'your_SSID'
PASSWORD = 'your_PASSWORD'

# Replace with your Flask server IP and port
SERVER_URL = 'http://your_server_ip:5000/upload'

# Connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        time.sleep(1)
    
    print('Connected to WiFi')
    print('IP:', wlan.ifconfig()[0])

# Capture image and send to server
def capture_and_send_image(camera_id):
    try:
        # Initialize camera
        esp32.camera_init()
        frame = esp32.camera_capture()

        if frame:
            print(f'Camera {camera_id} - Captured image')

            headers = {'Content-Type': 'image/jpeg'}
            response = urequests.post(SERVER_URL, data=frame, headers=headers)
            print(f'Response: {response.status_code}, {response.text}')
            response.close()

        gc.collect()

    except Exception as e:
        print(f'Failed to capture or send image: {e}')

def main():
    camera_id = 'camera_1'  # Unique ID for this camera
    connect_wifi(SSID, PASSWORD)
    while True:
        capture_and_send_image(camera_id)
        time.sleep(10)

if __name__ == '__main__':
    main()
