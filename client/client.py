import socket

from client.hmac_utils import generate_hmac
from shared.config import HOST, PORT

while True:
    message = input("Write message: ")

    if message.lower() == "exit":
        break

    if "|" in message:
        print("Message cannot contain | character.")
        continue

    generated_hmac = generate_hmac(message)
    data = f"{message}|{generated_hmac}"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            client.sendall(data.encode())

            response = client.recv(1024).decode()
            print(f"Server response: {response}")

    except ConnectionRefusedError:
        print("Could not connect to server. Make sure server.py is running.")
