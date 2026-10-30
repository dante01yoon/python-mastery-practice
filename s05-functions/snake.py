import random
import turtle

screen = turtle.Screen()
screen.title("스네이크")
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

head = turtle.Turtle("square")
head.color("lime")
head.penup()
direction = "stop"

food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)

body = []
score = 0


def go_up():
    global direction
    if direction != "down":
        direction = "up"


def go_down():
    global direction
    if direction != "up":
        direction = "down"


def go_left():
    global direction
    if direction != "right":
        direction = "left"


def go_right():
    global direction
    if direction != "left":
        direction = "right"


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


def move():
    x, y = head.xcor(), head.ycor()
    if direction == "up":
        head.sety(y + 20)
    elif direction == "down":
        head.sety(y - 20)
    elif direction == "left":
        head.setx(x - 20)
    elif direction == "right":
        head.setx(x + 20)


def game_over():
    pen.goto(0, 0)
    pen.write("게임 끝", align="center", font=("Arial", 36, "bold"))


def tick():
    global score
    old = head.position()
    move()

    if abs(head.xcor()) > 280 or abs(head.ycor()) > 280:
        game_over()
        return

    for part in body:
        if head.distance(part) < 10:
            game_over()
            return

    if head.distance(food) < 20:
        food.goto(random.randint(-13, 13) * 20, random.randint(-13, 13) * 20)
        part = turtle.Turtle("square")
        part.color("green")
        part.penup()
        body.append(part)
        score += 1

    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].position())
    if body:
        body[0].goto(old)

    pen.clear()
    pen.write(f"점수 {score}", align="center", font=("Arial", 20, "normal"))
    screen.update()
    screen.ontimer(tick, 120)


tick()
screen.mainloop()
