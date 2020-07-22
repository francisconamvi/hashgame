from tkinter import *

class gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("HashGame")
        self.window.geometry("+300+300")
        self.window.resizable(width=False, height=False)

        self.last_pos = [IntVar(),IntVar()]

        self.b = [[None]*3 for x in range(3)]
        for i in range(3):
            for j in range(3):
                if(i==0 and j==0):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(0,0))
                elif(i==0 and j==1):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(1,0))
                elif(i==0 and j==2):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(2,0))
                elif(i==1 and j==0):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(0,1))
                elif(i==1 and j==1):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(1,1))
                elif(i==1 and j==2):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(2,1))
                elif(i==2 and j==0):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(0,2))
                elif(i==2 and j==1):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(1,2))
                elif(i==2 and j==2):
                    self.b[i][j] = Button(self.window, text=" ", state="disabled", command = lambda: self.get_position(2,2))
        self.status = Label(self.window, text= "status")
        self.last_pos[0].set(-1)
        self.last_pos[1].set(-1)

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

    def enable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.b[i][j]["state"] = "normal"
        self.last_pos[0].set(-1)
        self.last_pos[1].set(-1)
        self.window.update()
    
    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.b[i][j]["state"] = "disabled"
        self.window.update()

    def get_position(self, x, y):
        self.last_pos[0].set(x)
        self.last_pos[1].set(y)

def main():
    my_gui = gui()
    my_gui.window.mainloop()

if __name__ == "__main__":
    main()