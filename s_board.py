import turtle
import time


def score_board_display(name, score, high_score):
    score_board = turtle.Turtle()
    score_board.penup()
    score_board.hideturtle()
    score_board.speed(0)
    score_board.color("blue")
    score_board.goto(0, 210)
    score_board.write(f'Name: {name} | Score: {score} | High Score: {high_score}', align="center", font=("System", 16, "normal"))
    score_board.clear()


def ending_score_board(name, high_score):
    score_board = turtle.Turtle()
    score_board.penup()
    score_board.hideturtle()
    score_board.speed(0)
    score_board.color("blue")
    score_board.goto(0, 0)
    score_board.write(f'    Good job {name}! \nYour High Score: {high_score}', align="center", font=("System", 18, "normal"))
    time.sleep(1.5)
    score_board.clear()
    score_board.write('Bye!', align="center", font=("System", 18, "normal"))
    time.sleep(1.5)



if __name__ == '__main__':
    score_board_display()