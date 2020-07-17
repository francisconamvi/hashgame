import socket
import time
from game_functions import *

#sockets configuration
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    print("Waiting for client connection")
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = pickle.dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket.send(msg)
    time.sleep(1)

    msg = "Waiting..."
    msg = pickle.dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket.send(msg)
    time.sleep(1)

    start_game(clientsocket, address)
    if(input("Go to next game? y or n ")=="n"):
        break
print("bye bye :)")