# Ülesanne 02
# 05.12.2024

import turtle

aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("olümpiarõngad mtursk")

turtle.speed(0)
turtle.pensize(6)


turtle.penup()
turtle.goto(-200,100)
turtle.pendown()

turtle.pencolor("blue")
turtle.circle(50,360)

turtle.penup()
turtle.goto(-150,50)
turtle.pendown()

turtle.pencolor("yellow")
turtle.circle(50,360)

turtle.penup()
turtle.goto(-100,100)
turtle.pendown()

turtle.pencolor("black")
turtle.circle(50,360)

turtle.penup()
turtle.goto(-50,50)
turtle.pendown()

turtle.pencolor("green")
turtle.circle(50,360)

turtle.penup()
turtle.goto(0,100)
turtle.pendown()

turtle.pencolor("red")
turtle.circle(50,360)











turtle.done()