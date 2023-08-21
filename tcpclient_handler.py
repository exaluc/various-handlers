import socket

class TCPClientHandler:
    """
    A TCP client handler class that provides an interface to send data
    to a specified domain and port using TCP.
    """

    def __init__(self, domain: str, port: int):
        """
        Initializes the TCP client with a domain and port.

        Args:
        - domain (str): The target domain or IP address.
        - port (int): The target port.
        """
        self.domain = domain
        self.port = port

    def send_data(self, data: str) -> str:
        """
        Sends data to the specified domain and port using a TCP connection.

        Args:
        - data (str): The data to send.

        Returns:
        - str: The response received after sending the data.
        """
        
        # Create a socket object. AF_INET indicates that we want an IPv4-based socket, 
        # and SOCK_STREAM indicates that this will be a TCP client.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            # Establish a connection to the specified domain and port.
            s.connect((self.domain, self.port))
            
            # Convert the data to bytes and send it over the connection.
            s.sendall(data.encode('utf-8'))
            
            # Wait for a response. Here, we are reading up to 1024 bytes. 
            # This can be adjusted based on expected response size.
            response = s.recv(1024)
            
        # Return the decoded response.
        return response.decode('utf-8')

# Create an instance of our TCP client handler.
client = TCPClientHandler("example.com", 12345)
    
# Send the data and retrieve the response.
response = client.send_data(data)
