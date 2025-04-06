import random
import socket

class GuessingGameServer:
    def __init__(self, host="0.0.0.0", port=7777):
        # Initialize server parameters
        self.host = host
        self.port = port
        self.secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.attempts = 0  # Track number of attempts

    def start(self):
        # Bind the server socket and start listening
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            conn, addr = self.server_socket.accept()  # Accept a new connection
            print(f"Connected by {addr}")
            self.attempts = 0  # Reset attempts for new connection

            with conn:
                while True:
                    data = conn.recv(1024).decode().strip()  # Receive data from client
                    if not data:
                        break  # Exit loop if client disconnects

                    try:
                        guess = int(data)  # Try to convert input to integer
                        self.attempts += 1  # Increment attempt count

                        # Compare the guess with the secret number
                        if guess < self.secret_number:
                            response = "Too low!"
                        elif guess > self.secret_number:
                            response = "Too high!"
                        else:
                            # Check performance based on attempt count
                            if self.attempts <= 5:
                                response = "Correct! Very good!"
                            elif self.attempts <= 10:
                                response = "Correct! Good!"
                            else:
                                response = "Correct! Fair!"

                            # Reset game after correct guess
                            self.secret_number = random.randint(1, 100)
                            self.attempts = 0

                        conn.sendall(response.encode())  # Send response back to client
                    except ValueError:
                        # Handle invalid input (non-integer)
                        conn.sendall("Invalid input! Please enter a number.".encode())

    def stop(self):
        # Close the server socket
        self.server_socket.close()

def main():
    server = GuessingGameServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server.stop()

if __name__ == "__main__":
    main()