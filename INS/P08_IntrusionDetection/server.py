import socket

threat_signatures = ['malware', 'exploit', 'ranjit', 'attack']
def hasMalware(data):
    for signature in threat_signatures:
        if signature in response.lower():
            print("\n!! WARNING: Potential danger from client.")
            print("Detected %s in response" %signature)
            return True

port = 8888
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', port))
sock.listen(5)
print("Server listening at http://127.0.0.1:%d" %port)

while True:
    try:
        clientsock, clientaddr = sock.accept()
        response = clientsock.recv(1024).decode()
        print("\n:: Recieved message from", clientaddr)
        print(response)

        if hasMalware(response):
            clientsock.send(b"Intrusion Detected. Shutting down...")
            clientsock.close()
            continue

        clientsock.send(b"Welcome to the server.")
        clientsock.close()

    except KeyboardInterrupt:
        print("Exiting server...")
        exit()
    except Exception as e:
        print("SERVER_ERROR:", e)

