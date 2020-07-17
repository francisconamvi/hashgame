import pickle
import time

HEADERSIZE = 10
def get_back(clientsocket):
    full_msg = b''
    new_msg = True
    while True:
        msg = clientsocket.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg
        if(len(full_msg)-HEADERSIZE == msglen):
            d = pickle.loads(full_msg[HEADERSIZE:])
            #tuple of x and y of player 2
            return d
            new_msg = True
            full_msg = b''


def print_board(board):
    for line in board:
        print(line)

def inicialize_board():
    return [[' ',' ',' '] for x in range(3)]

def start_game(clientsocket, address):
    board = inicialize_board()
    print("Give X and Y position")
    print("Exemple -> Player 1: 1 1")

    while True:
        print()
        print_board(board)
        player_input = tuple(map(int, input("Player 1: ").split()))
        while(not set_board(board, player_input, 1)):
            print("Invalid position. Try again!")
            player_input = tuple(map(int, input("Player 1: ").split()))

        if(gameover(board)):
            msg = "Player 1 wins!"
            print(msg)
            print_board(board)

            msg = pickle.dumps(msg)
            msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
            clientsocket.send(msg)
            time.sleep(1)

            msg = pickle.dumps(board)
            msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
            clientsocket.send(msg)
            time.sleep(1)

            break
        
        #send actual board to player2
        msg = pickle.dumps(board)
        msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
        clientsocket.send(msg)
        set_board(board, get_back(clientsocket), 2)

        if(gameover(board)):
            msg = "Player 2 wins!"
            print(msg)
            print_board(board)

            msg = pickle.dumps(msg)
            msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
            clientsocket.send(msg)
            time.sleep(1)

            msg = pickle.dumps(board)
            msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
            clientsocket.send(msg)
            time.sleep(1)

            break
        

def set_board(board, player_input, player):
    if(len(player_input) != 2):
        return False
    p = [0,0]
    p[0], p[1] = player_input[1], player_input[0]
    if(p[0] > 2 or p[0] < 0 or p[1] > 2 or p[1] < 0):
        return False

    if(board[p[0]][p[1]] == ' '):
        if(player == 1):
            board[p[0]][p[1]] = 'X'
        else:
            board[p[0]][p[1]] = 'O'
        return True
    else:
        return False


def gameover(board):
    #line
    for line in board:
        if (line[0] == line[1] == line[2]) and line[0] != ' ':
            return True
    #column
    for i in range(3):
        if(board[0][i] == board[1][i] == board[2][i]) and board[0][i] != ' ':
            return True

    #diagonal
    if(board[0][0] == board[1][1] == board[2][2]) and board[0][0] != ' ':
        return True
    if(board[0][2] == board[1][1] == board[2][0]) and board[2][0] != ' ':
        return True    

    return False

