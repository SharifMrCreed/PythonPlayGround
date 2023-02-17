from tkinter import *
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = "000000"
SPACE_SIZE = 20
FOOD_COLOR = "#FFFF00"
SNAKE_COLOR = "#00FF00"
SNAKE_LENGTH = 3
DIRECTION = "down"
GAME_SPEED = 24


class Snake:
    def __init__(self):
        self.body_parts = []
        self.coordinates = []
        for length in range(SNAKE_LENGTH):
            self.coordinates.append([0, 0])
        next_turn(self)

    def move(self, direction):
        # create a new head
        xh, yh = self.coordinates[0]

        if direction == "right":
            xh += SPACE_SIZE
        elif direction == "left":
            xh -= SPACE_SIZE
        elif direction == "up":
            yh -= SPACE_SIZE
        else:
            yh += SPACE_SIZE
        self.coordinates.insert(0, [xh, yh])
        self.coordinates.pop(-1)


class Food:
    def __init__(self):
        x_coordinate = random.randint(0, SCREEN_WIDTH - SPACE_SIZE)
        y_coordinate = random.randint(0, SCREEN_HEIGHT - SPACE_SIZE)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


def draw_food():
    food = Food()
    canvas.create_oval(food.x_coordinate, food.y_coordinate,
                       food.x_coordinate + SPACE_SIZE,
                       food.y_coordinate + SPACE_SIZE,
                       fill=FOOD_COLOR)


def draw_snake(_snake):
    for x, y in _snake.coordinates:
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")


def next_turn(_snake):
    _snake.move(DIRECTION)
    draw_snake(_snake)
    window.after(GAME_SPEED, next_turn, _snake)


window = Tk()

label = Label(text="Ssssnakeeeee", font=("Roboto", 28))
label.pack()

canvas = Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

snake = Snake()
draw_food()

window.mainloop()
