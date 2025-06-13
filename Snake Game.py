import turtle 
import time 
import random

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

snake = []
start_length = 3

for i in range(start_length):
    part = turtle.Turtle()
    part.shape("square")
    part.color("green")
    part.penup()
    part.goto(-20*i, 0)
    snake.append(part)

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 0)

direction = "stop"

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

win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

def move():
    if direction == "up":
        y = snake[0].ycor()
        snake[0].sety(y + 20)
    if direction == "down":
        y = snake[0].ycor()
        snake[0].sety(y - 20)
    if direction == "left":
        x = snake[0].xcor()
        snake[0].setx(x - 20)
    if direction == "right":
        x = snake[0].xcor()
        snake[0].setx(x + 20)

while True:
    win.update()
    move()

   
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)

 
    if snake[0].distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        part = turtle.Turtle()
        part.shape("square")
        part.color("green")
        part.penup()
        snake.append(part)

  
    if abs(snake[0].xcor()) > 290 or abs(snake[0].ycor()) > 290:
        print("Game Over")
        break

   
    for segment in snake[1:]:
        if snake[0].distance(segment) < 20:
            print("Game Over")
            break

    time.sleep(0.1)

win.mainloop()
