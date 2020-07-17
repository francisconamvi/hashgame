import socket
import pickle
from game_functions import *

#sockets configuration
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1235))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg
        if(len(full_msg)-HEADERSIZE == msglen):
            d = pickle.loads(full_msg[HEADERSIZE:])
            if(isinstance(d, str)):
                print(d)
            elif(isinstance(d, list)):
                print_board(d)
                board = d
                if(gameover(board)):
                    quit()
                player_input = tuple(map(int, input("Player 2: ").split()))
                while(not set_board(board, player_input, 2)):
                    print("Invalid position. Try again!")
                    player_input = tuple(map(int, input("Player 2: ").split()))
                #send to server player input
                msg = pickle.dumps(player_input)
                msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
                s.send(msg)

            new_msg = True
            full_msg = b''