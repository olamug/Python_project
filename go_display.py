import turtle
import time
import random


def game_over_display():
    tekst = 'GAME OVER'
    display = turtle.Turtle()
    display.hideturtle()
    display.speed(0)
    colors = ["DodgerBlue", "Aquamarine", "SpringGreen", "GreenYellow", "Fuchsia", "DeepSkyBlue"]
    for e in range(5):
        display.color(random.choice(colors))
        display.write(tekst, align='center', font=("Arial", 25, "bold"))
        time.sleep(0.5)
    display.clear()


if __name__ == '__main__':
    game_over_display()