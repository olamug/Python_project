import turtle
import time
import random
from go_display import game_over_display
from s_board import score_board_display, ending_score_board
from welcome import welcome_display


def move():
    if joe.direction == 'up':
        y = joe.ycor()
        joe.sety(y+10)
        if joe.ycor() == 250:
            joe.sety(-250)
    if joe.direction == 'down':
        y = joe.ycor()
        joe.sety(y-10)
        if joe.ycor() == -250:
            joe.sety(250)
    if joe.direction == 'left':
        x = joe.xcor()
        joe.setx(x-10)
        if joe.xcor() == -250:
            joe.setx(250)
    if joe.direction == 'right':
        x = joe.xcor()
        joe.setx(x+10)
        if joe.xcor() == 250:
            joe.setx(-250)
    if joe.direction == 'stop':
        joe.direction = 'stop'
        for body in stomach:
            body.direction = 'stop'
    if joe.pos == (666, 666):
        game_over_display()



def go_up():
    if joe.direction != 'down':
        joe.direction = "up"


def go_down():
    if joe.direction != 'up':
        joe.direction = "down"


def go_left():
    if joe.direction != 'right':
        joe.direction = "left"


def go_right():
    if joe.direction != 'left':
        joe.direction = "right"


def stop():
    joe.direction = 'stop'


def end_of_game():
    joe.setpos(666, 666)
    game_over_display()
    ending_score_board(players_name, high_score)
    exit()


# stworzenie okna i jego cech
wn = turtle.Screen()
wn.title("Snake 1.0")
wn.bgcolor("Thistle")
wn.setup(width=500, height=500)
wn.tracer(0)

# stworzenie głowy węża - Joe
joe = turtle.Turtle()
joe.speed(0)  # na razie nie potrzebuje się poruszać
joe.shape("square")
joe.color("black")
joe.penup()  # podnosimy ołówek, żeby nie zostawiać śladu po głowie
joe.goto(0, 0)  # ustawiamy joe na pozycji zerowej
joe.direction = "stop"

# stworzenie jedzenia
food = turtle.Turtle()
food.shape("circle")
food.color("DeepPink")
food.penup()  # podnosimy ołówek, żeby nie zostawiać śladu
xr = random.randrange(-240, 240, 10)
yr = random.randrange(-240, 240, 10)
food.goto(xr, yr)

# przypisanie klawiszy do ruchu
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(stop, " ")
wn.onkeypress(end_of_game, "x")


delay = 0.05
score = 0
high_score = 0
stomach = []

welcome_display()
players_name = input("What's your name? \n")


while True:
    wn.update()
    score_board_display(players_name, score, high_score)

    # zmiana miejsca jedzenia
    if joe.pos() == food.pos():
        x = random.randrange(-240, 240, 10)
        y = random.randrange(-240, 240, 10)
        food.goto(x, y)

        # stworzenie ciała joe, czyli obiekt 'body'
        body = turtle.Turtle()
        body.speed(0)
        body.shape('square')
        body.color('grey')
        body.penup()
        stomach.append(body)
        score += 10
        if score > high_score:
            high_score = score
        delay -= 0.0005

    for index in range(len(stomach) - 1, 0, -1):
        x = stomach[index - 1].xcor()
        y = stomach[index - 1].ycor()
        stomach[index].goto(x, y)

    if len(stomach) > 0:
        x = joe.xcor()
        y = joe.ycor()
        stomach[0].goto(x, y)

    move()  # po każdym update uruchamiamy funkcję

    for body in stomach:
        if joe.pos() == body.pos():
            time.sleep(0.5)
            stop()
            joe.goto(0, 0)
            for body in stomach:
                body.hideturtle()
            stomach.clear()
            game_over_display()
            score = 0
    time.sleep(0.01)
    time.sleep(delay)


