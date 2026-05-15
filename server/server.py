import socket
import threading

from server.verifier import verify_hmac
from shared.config import HOST, PORT

def handle_client(client_socket):
    print("client connected.")

    try:
        data=client_socket.recv(1024).decode()
        parts = data.split("|")

        if len(parts) != 2:
            client_socket.send("Invalid message format.".encode())
            return

        message, received_hmac = parts

        print(f"received Message: {message}")
        print(f"received hmac: {received_hmac}")

        if(verify_hmac(message,received_hmac)):
            response="message verified"
            print("hmac is valid!")

        else:
            response="message tampered"
            print("hmac verificaition failed")

        client_socket.send(response.encode())
    
    except Exception as error:
        print(f"error: {error} ")

    finally:
        client_socket.close()
        print("client disconnected")

        

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server.bind((HOST,PORT))

server.listen()

print(f"server listening on {HOST}:{PORT}")

while True:
    client_socket,address=server.accept()

    print(f"connection from {address}")

    client_thread=threading.Thread(
        target=handle_client,
        args=(client_socket,)
 
    )

    client_thread.start()