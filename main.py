import turtle, time

# zainicjowanie okna ze swoimi cechami
# zmienna dla turtle.Screen() = wn
wn = turtle.Screen()
wn.title("Snake 1.0")
wn.bgcolor("Thistle")
wn.setup(width=500, height=500)
wn.tracer(0)  # wyłączamy animacje

# stworzenie głowy węża, głowa mojego węża nazywa się joe
joe = turtle.Turtle()
joe.speed(0)  # narazie nie potrzebuje się poruszać
joe.shape("turtle")
joe.color("black")
joe.penup()  # podnosimy ołówek, żeby nie zostawiać śladu po głowie
joe.goto(0,0)  # ustawiamy joe na pozycji zerowej
joe.direction = "stop"

# stworzenie jedzenia dla joe, jedzenie to corn (to też turtle)


