from tkinter import *
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = "000000"
SPACE_SIZE = 20
FOOD_COLOR = "#FFFF00"
SNAKE_COLOR = "#00FF00"
SNAKE_LENGTH = 3
DIRECTION = "right"
GAME_SPEED = 90
score = 0


class Snake:
    def __init__(self):
        self.body_parts = []
        self.coordinates = []
        for length in range(SNAKE_LENGTH):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            self.body_parts.append(
                canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            )
        global food
        food = Food()
        next_turn(self, food)

    def move(self, direction, _food):
        # create a new head
        global score
        coincides = False
        xh, yh = self.coordinates[0]

        if xh == _food.x_coordinate and yh == _food.y_coordinate:
            score += 1
            canvas.delete("food")
            global food
            food = Food()
            draw_food(food)
            coincides = True
        else:
            coincides = False

        if direction == "right":
            xh += SPACE_SIZE
        elif direction == "left":
            xh -= SPACE_SIZE
        elif direction == "up":
            yh -= SPACE_SIZE
        else:
            yh += SPACE_SIZE

        self.body_parts.insert(
            0, canvas.create_rectangle(xh, yh, xh + SPACE_SIZE, yh + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
        )

        if coincides is False:
            self.coordinates.pop()
            canvas.delete(self.body_parts[-1])
            self.body_parts.pop()
        self.coordinates.insert(0, [xh, yh])


class Food:
    def __init__(self):
        x_coordinate = random.randint(0, int(SCREEN_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y_coordinate = random.randint(0, int(SCREEN_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


def draw_food(_food):
    canvas.create_oval(_food.x_coordinate, _food.y_coordinate,
                       _food.x_coordinate + SPACE_SIZE,
                       _food.y_coordinate + SPACE_SIZE,
                       fill=FOOD_COLOR, tags="food")


def change_direction(direction):
    global DIRECTION
    if DIRECTION == "left" or DIRECTION == "right":
        if direction != "left" and direction != "right":
            DIRECTION = direction
    else:
        if direction != "up" and direction != "down":
            DIRECTION = direction


def next_turn(_snake, _food):
    _snake.move(DIRECTION, _food)
    window.after(GAME_SPEED, next_turn, _snake, _food)


window = Tk()
window.bind('<Left>', lambda event: change_direction("left"))
window.bind('<Right>', lambda event: change_direction("right"))
window.bind('<Up>', lambda event: change_direction("up"))
window.bind('<Down>', lambda event: change_direction("down"))

label = Label(text="Ssssnakeeeee", font=("Roboto", 28))
label.pack()

canvas = Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

snake = Snake()
food = Food()
draw_food(food)

window.mainloop()
