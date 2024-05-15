import socket

HOST = "192.168.0.14"  # Replace with the target PC's IP address
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, this is a notification from the source PC")
    print("Notification sent successfully")