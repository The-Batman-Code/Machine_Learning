from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
boxes = []
screen.tracer(0)

for i in range(3):
    batman = Turtle('square')
    batman.color('white')
    batman.penup()
    batman.goto(-20*i, 0)
    batman.speed(0)
    boxes.append(batman)
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for bats in boxes:
        bats.forward(20)
screen.exitonclick()
