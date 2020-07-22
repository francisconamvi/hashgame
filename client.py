import socket
import pickle
from game_functions import *
from tkinter import *
from gui import *

#sockets configuration
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1235))

hash_gui = gui()

while True:
    hash_gui.window.update_idletasks()
    hash_gui.window.update()
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
                hash_gui.set_status(d)
            elif(isinstance(d, list)):
                print_board(d)
                board = d
                if(p1_turn(board)):
                    player = 1
                else:
                    player = 2
                hash_gui.update_board(board)
                if(gameover(board)):
                    hash_gui.window.mainloop()
                    quit()
                hash_gui.enable_buttons()
                hash_gui.window.wait_variable(hash_gui.last_pos[0])
                player_input = (hash_gui.last_pos[0].get(), hash_gui.last_pos[1].get())
                print(player_input)
                while(not set_board(board, player_input, player)):
                    hash_gui.set_status("Invalid move. Try again")
                    hash_gui.window.wait_variable(hash_gui.last_pos[0])
                    player_input = (hash_gui.last_pos[0].get(), hash_gui.last_pos[1].get())
                    print(player_input)
                hash_gui.disable_buttons()
                hash_gui.update_board(board)
                #send to server player input
                msg = pickle.dumps(player_input)
                msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
                s.send(msg)

            new_msg = True
            full_msg = b''