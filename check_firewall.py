import socket

def send_data_through_interface(interface, target_ip, target_port):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to the specific interface
    s.bind((interface, 0))

    try:
        # Connect to a target IP and port through the specific interface
        s.connect((target_ip, target_port))
        print(f"Successfully connected to {target_ip}:{target_port} through {interface}")
        
        # Optionally send some data here
        s.sendall(b"Hello, Server!")
        data = s.recv(1024)
        print("Received:", repr(data))

    except Exception as e:
        print(f"Failed to connect to {target_ip}:{target_port} through {interface}. Error: {e}")

    finally:
        s.close()

# Example usage:
interface_ip = "your_interface_ip"  # IP of the interface you want to use
target_ip = "target_server_ip"
target_port = 80  # Example: Port 80 for HTTP

send_data_through_interface(interface_ip, target_ip, target_port)
