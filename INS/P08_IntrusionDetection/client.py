import socket

# Server script for testing
server_port = 8888
server_ip = '127.0.0.1'

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {server_ip}:{server_port}...")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established!")

    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

    # Send a response back to the client
    client_socket.send(b"Hello from server.")

    # Close the connection
    client_socket.close()