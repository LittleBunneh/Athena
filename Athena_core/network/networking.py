# Networking and distributed agent protocols.
import socket

class NetworkAgent:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print(f"NetworkAgent listening on {self.host}:{self.port}")
        conn, addr = self.sock.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        print(f"Received: {data.decode()}")
        conn.close()

    def send_message(self, message, target_host='localhost', target_port=5000):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_host, target_port))
            s.sendall(message.encode())
            print(f"Sent: {message}")

if __name__ == "__main__":
    # Example usage: run start_server() in one process, send_message() in another
    pass
