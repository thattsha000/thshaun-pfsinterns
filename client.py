import os
import socket
import threading
from PIL import Image
from io import BytesIO

run = 0
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('ADDRESS', PORTNUMBER))
client.connect
def process_qr_code(image_data):
    try:
        # Convert binary data to an image
        image = Image.open(BytesIO(image_data))
        print("New QR Code received from server:")
        image.show()  # Display the image
    except Exception as e:
        print(f"Error opening image: {e}")

def receive(client):
    while True:
        try:
            data = client.recv(4096)
            if not data:
                break  # Connection closed
            print(f"New Message Received: {data.decode().strip()}")
        except Exception as e:
            print(f"Error occurred: {e}")
            break
    client.close()


def send(client):
    while True:
        command = input("Enter command (UPLOAD, DONE): ").strip().upper()
        if command == "UPLOAD":
            file_path = input("Enter the file path that you would like to upload: ").strip()
            filename = os.path.basename(file_path)
            client.sendall(b'UPLOAD')
            client.sendall(filename.encode())

            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    client.sendall(data)

            client.shutdown(socket.SHUT_WR)
            print(f"File {filename} was uploaded to the server.")

        elif command == "DONE":
            client.sendall(b'DONE')
            break

    client.close()


receive_thread = threading.Thread(target=receive, args=(client,))
send_thread = threading.Thread(target=send, args=(client,))
receive_thread.start()
send_thread.start()

