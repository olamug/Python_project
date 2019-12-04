import turtle
import time
import random


def game_over_display():
    tekst = 'GAME OVER'
    go_display = turtle.Turtle()
    go_display.hideturtle()
    go_display.speed(0)
    colors = ["DodgerBlue", "Aquamarine", "SpringGreen", "GreenYellow", "Fuchsia", "DeepSkyBlue"]
    for e in range(5):
        go_display.color(random.choice(colors))
        go_display.write(tekst, align='center', font=("System", 25, "normal"))
        time.sleep(0.5)
    go_display.clear()


if __name__ == '__main__':
    game_over_display()