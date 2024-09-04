import os
import socket
import threading

host = 'HOST'
port = "PORTNUMBER"
srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvsock.bind((host, port))
srvsock.listen(5)
uploads_dir = 'COMMONDIRECTORYTOUPLOAD'


if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

print('Server Socket Running')



def handle(client):
    filename = ""
    while True:
        command = client.recv(4096).decode().strip()
        if command == 'UPLOAD':
            filename = client.recv(4096).decode().strip()
            path = os.path.join(uploads_dir, filename)
            with open(path, 'wb') as f:
                number_ran = 0
                while True:
                    data: bytes = client.recv(1024)
                    print(number_ran)
                    number_ran += 1
                    print(data)
                    if not data:
                        break
                    f.write(data)
            print(f"File {filename} has been uploaded to the server.")
        elif command == "DONE":
            break

        file_url = f"http://{host}:{port}/downloads/{filename}"
        client.sendall('Message from Server: File has been uploaded and a file url has been generated'.encode())
    client.close()


def receive():
    while True:
        client, address = srvsock.accept()
        print(f"Connected with {str(address)} ")
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is now listening for new file uploads")
receive()
