from tkinter import *
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = "000000"
FOOD_SIZE = 50
SNAKE_SIZE = 50


class Snake:
    pass


class Food:
    __init__(self):


window = Tk()

label = Label(text="Ssssnakeeeee", font=("Roboto", 28))
label.pack()

canvas = Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

snake = Snake()
food = Food()

canvas.create_oval(food.xCoordinate, food.yCoordinate, FOOD_SIZE, FOOD_SIZE)

window.mainloop()
