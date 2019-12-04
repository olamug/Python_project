import turtle
import time
import random


def welcome_display():
    colors = ["DodgerBlue", "SpringGreen", "GreenYellow", "Fuchsia", "DeepSkyBlue"]
    welcome = turtle.Turtle()
    welcome.penup()
    welcome.hideturtle()
    welcome.speed(0)
    welcome.color(random.choice(colors))
    welcome.goto(0, 0)
    welcome.write(f'              Welcome to snake 1.0! '
                  f'\nCollect all items and become a master. '
                  f'\n         Press x to exit the game.', align="center", font=("System", 14, "normal"))
    time.sleep(2.5)
    welcome.clear()