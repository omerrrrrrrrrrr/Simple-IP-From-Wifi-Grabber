# Simple-IP-From-Wifi-Grabber 📡

A Python tool to find IP and MAC addresses of devices on your Wi-Fi.

## Setup 🚀

1. Install Python 3.
2. Install Scapy:
   ```bash
   pip install -r requirements.txt
   ```

## Run ✅

- **Windows**: Open terminal as Administrator, then:
  ```bash
  python main.py
  ```
- **Linux/macOS**: Use sudo:
  ```bash
  sudo python3 main.py
  ```

## Notes 🔍

- Scans `192.168.1.0/24` by default. Edit `main.py` if your network is different.
- Look for your PC’s MAC or IP in the results.