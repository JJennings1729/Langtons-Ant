import tkinter as tk
import numpy as np

Width = 300
Height = 180
SquareSize = 5

global AntWalking 
AntWalking = True

root = tk.Tk()
root.attributes('-fullscreen', True)
canvas = tk.Canvas(root, width=Width*SquareSize, height=Height*SquareSize, bg='black')
canvas.pack()

class Board ():

    def __init__ (self, size):
        self.board = np.array([0] * size[0] * size[1])
    
    def DrawSquare (self, square):
        color = "white"
        if (self.board[square]):
            color = "black"
        x = square % Width
        y = np.floor(square/Width)
        canvas.create_rectangle(x*SquareSize, y*SquareSize, (x+1)*SquareSize, (y+1)*SquareSize, fill=color)

    def DrawBoard (self):
        for square in range(len(self.board)):
            self.DrawSquare(square)

GameBoard = Board((Width, Height))
GameBoard.DrawBoard()
root.update()

class Ant ():

    def __init__ (self, start):   # start is a number representing the beginning square
        self.pos = start
        self.heading = [0, 1]     # Direction we're heading

    def Move (self):
        if (GameBoard.board[self.pos]):                               # If 1, turn left. Otherwise turn right.
            self.heading = [-self.heading[1], self.heading[0]]
        else:
            self.heading = [self.heading[1], -self.heading[0]]
        GameBoard.board[self.pos] = int(not GameBoard.board[self.pos])
        GameBoard.DrawSquare(self.pos)
        self.pos += np.dot(self.heading, [1, Width])
        if (not 0 < self.pos < len(GameBoard.board)):
            print("Out of bounds")
            Close()

def Close():
    print("SHUTTING DOWN")
    root.quit()
    root.destroy()
    global AntWalking
    AntWalking = False
root.protocol("WM_DELETE_WINDOW", Close)

ant = Ant(21200)
while (AntWalking):
    ant.Move()
    root.update_idletasks()