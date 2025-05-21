# PIN Brute Force Client (Socket-Based)

This Python script performs a brute-force attack to guess a 3-digit PIN by sending HTTP POST requests to a server running on `127.0.0.1` (localhost) at port `8888`. It uses raw sockets to send requests and checks the response for the phrase **"Access granted"** to identify the correct PIN.

## 🔧 Requirements

- Python 3.x
- A local server listening on port `8888` that accepts POST requests with a `pin` field

## 📄 How It Works

1. Iterates through all 3-digit PINs from `000` to `999`.
2. Sends a POST request for each PIN using a raw socket connection.
3. Waits for the response and checks if it contains the phrase `"Access granted"`.
4. Stops when the correct PIN is found.

## 🚀 Running the Script

```bash
python pin_bruteforce.py
