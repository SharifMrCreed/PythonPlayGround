import random
from tkinter import *


def new_game():
    global aMoves
    global bMoves
    global game

    aMoves = []
    bMoves = []
    label.config(text=f"It's {player}'s turn")
    game = True

    for r in range(3):
        for cl in range(3):
            buttons[r][cl].config(text="")


def check_winner():
    global game
    if confirm_combination(aMoves):
        label.config(text=f"{players[0]} Wins")
        game = False
    elif confirm_combination(bMoves):
        label.config(text=f"{players[1]} Wins")
        game = False
    elif len(aMoves) + len(bMoves) == 9:
        label.config(text=f"Its a Tie")
        game = False
    else:
        label.config(text=f"It's {player}'s turn")


def map_move(_row, _col):
    if _row == 0:
        if _col == 0:
            return 0
        elif _col == 1:
            return 1
        else:
            return 2
    elif _row == 1:
        if _col == 0:
            return 3
        elif _col == 1:
            return 4
        else:
            return 5
    else:
        if _col == 0:
            return 6
        elif _col == 1:
            return 7
        else:
            return 8


def confirm_combination(moves_list):
    count = 0
    if len(moves_list) < 3:
        return False
    else:
        for c in winningCombinations:
            for n in c:
                if moves_list.__contains__(n):
                    count += 1
            if count > 2:
                return True
            count = 0
    return False


def next_turn(_row, _col):
    global game
    global player
    if game:
        btn = buttons[_row][_col]
        if btn['text'] == "":
            btn['text'] = player
            buttons[_row][_col] = btn
            check_winner()

            if player == players[0]:
                player = players[1]
                aMoves.append(map_move(_row, _col))

            else:
                bMoves.append(map_move(_row, _col))
                player = players[0]
            check_winner()


window = Tk()
window.title("Tic Tac Toe")

players = ["X", "O"]
aMoves = []
bMoves = []
player = random.choice(players)
game = True

winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 4, 8],
    [2, 4, 6],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8]
]

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text=f"It's {player}'s turn")
label.pack(side="top")

new_game_button = Button(text="New Game", command=lambda: new_game())
new_game_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        bttn = Button(frame, text="", width=5, height=2, command=lambda _row=row, _col=col: next_turn(_row, _col))
        bttn.grid(row=row, column=col)
        buttons[row][col] = bttn

window.mainloop()
