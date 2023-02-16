import random
from tkinter import *
from Game import *

window = Tk()
window.title("Tic Tac Toe")

players = ["X", "O"]
player = random.choice(players)

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text=f"It's {player}'s turn")
label.pack(side="top")

new_game_button = Button(text="New Game", command=new_game())
new_game_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        bttn = Button(frame, text="", width=5, height=2)
        bttn.grid(row = row, column= col)
        buttons[row][col] = bttn

window.mainloop()
