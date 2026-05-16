import socket

from client.hmac_utils import generate_hmac
from shared.config import HOST, PORT

# mesazhi origjinal
original_message = "Hello Server"

# gjenerimi i HMAC per mesazhin origjinal
valid_hmac = generate_hmac(original_message)

# simulimi i sulmit
tampered_message = "Hacked Message"

# dergohet mesazhi i ndryshuar me HMAC-in origjinal
data = f"{tampered_message}|{valid_hmac}"

# krijimi i socket-it
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lidhja me serverin
client.connect((HOST, PORT))

print("Sending tampered message...")

# dergimi i te dhenave
client.send(data.encode())

# marrja e pergjigjes nga serveri
response = client.recv(1024).decode()

print(f"Server response: {response}")

# mbyllja e lidhjes
client.close()