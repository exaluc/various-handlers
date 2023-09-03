import socket
import logging

class TCPClientHandler:
    def __init__(self, domain: str, port: int):
        self.domain = domain
        self.port = port

    def send_data(self, data: str):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)  # 5 seconds timeout for connecting and sending
                s.connect((self.domain, self.port))
                s.sendall(data.encode('utf-8'))
        except socket.timeout:
            logging.error(f"Timeout occurred while connecting to {self.domain}:{self.port}")
        except socket.error as e:
            logging.error(f"Socket error occurred: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

# Sample usage
if __name__ == "__main__":
    client = TCPClientHandler("example.com", 12345)
    client.send_data("your_data_here")
