from tkinter import *

class gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("HashGame")
        self.window.geometry("+300+300")
        self.window.resizable(width=False, height=False)

        self.b = [[None]*3 for x in range(3)]
        for i in range(3):
            for j in range(3):
                self.b[i][j] = Button(self.window, text=" ")
        self.status = Label(self.window, text= "status")

        for i in range(3):
            for j in range(3):
                self.b[i][j].grid(row=i,column=j,ipadx=20,ipady=20)
        self.status.grid(row=3,column=0,columnspan=3)

    def set_status(self, msg):
        self.status['text'] = msg
        self.window.update()

    def update_board(self, board):
        for i in range(3):
            for j in range(3):
                self.b[i][j]['text'] = board[i][j]
        self.window.update()

def main():
    my_gui = gui()
    my_gui.window.mainloop()

if __name__ == "__main__":
    main()