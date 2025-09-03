import turtle, random

sc = None
t1 = None
t2 = None
win = False

def setup():
    global sc, t1, t2 
    sc = turtle.Screen()
    sc.setup(500, 500)
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.color("red")
    t2.color("green")
    t1.shape("turtle")
    t2.shape("turtle")
    t1.penup()
    t2.penup()
    t1.goto(-150, 50)
    t2.goto(-150, -50)

def start_race():
    global win
    for i in range(100):
        if not win:
            t1.forward(random.randint(1, 5))
            t2.forward(random.randint(1, 5))
            check_winner()
        else:
            break

def check_winner():
    global win
    if t1.xcor() > 150:
        print("t1 won")
        win = True
    if t2.xcor() > 150:
        print("t2 won")
        win = True

setup()
start_race()