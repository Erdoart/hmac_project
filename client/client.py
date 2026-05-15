import socket

from client.hmac_utils import generate_hmac
from shared.config import HOST, PORT

# krijimi i socket-it
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lidhja me serverin
client.connect((HOST, PORT))

print("Connected to server!")

while True:

    # input nga useri
    message = input("Write message: ")

    # me dal prej programit
    if message.lower() == "exit":
        break

    # gjenerimi i HMAC
    generated_hmac = generate_hmac(message)

    # kombinimi i message + hmac
    data = f"{message}|{generated_hmac}"

    # dergimi te serveri
    client.send(data.encode())

    # marrja e pergjigjes
    response = client.recv(1024).decode()

    print(f"Server response: {response}")

# mbyllja e lidhjes
client.close()