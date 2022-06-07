import turtle

s = turtle.getscreen()

turtle.title("My First Turtle Program from Alex")

turtle.bgcolor("red")
turtle.shapesize(3, 3, 3)
turtle.fillcolor("blue")
turtle.shape("turtle")

turtle.pen(pencolor="white", pensize=6, speed=4)

turtle.penup()
turtle.forward(150)
turtle.rt(90)
turtle.pendown()


for i in range(4):
    turtle.forward(300)
    turtle.right(90)


turtle.penup()
turtle.forward(150)
turtle.rt(90)
turtle.forward(150)
turtle.pendown()

turtle.pen(pencolor="blue", pensize=6, speed=14)

for i in range(4):
    turtle.forward(50)
    turtle.right(90)
for i in range(4):
    turtle.backward(50)
    turtle.right(90)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
for i in range(4):
    turtle.backward(50)
    turtle.left(90)

turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
turtle.right(120)

turtle.pen(pencolor="white", fillcolor="blue",  pensize=6, speed=10)
turtle.begin_fill()
for i in range(3):
    turtle.forward(300)
    turtle.right(120)
turtle.end_fill()


turtle.penup()
turtle.goto(250, 200)
turtle.pendown()

turtle.pen(pencolor="yellow", pensize=6, speed=15)
for i in range(12):
    turtle.circle(30)
    turtle.right(150)

turtle.penup()
turtle.goto(350, -100)
turtle.right(60)
turtle.pendown()


turtle.pen(pencolor="white", fillcolor="green",  pensize=6, speed=3)

turtle.begin_fill()

for i in range(3):
    turtle.forward(50)
    turtle.left(120)
turtle.end_fill()

turtle.penup()

turtle.forward(25)
turtle.right(60)
turtle.pendown()


turtle.begin_fill()
for i in range(3):
    turtle.forward(75)
    turtle.right(120)
turtle.end_fill()

turtle.penup()
turtle.forward(75)
turtle.right(120)
turtle.forward(37.5)
turtle.left(60)
turtle.pendown()

turtle.begin_fill()
for i in range(3):
    turtle.forward(130)
    turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.goto(-300, -250)
turtle.right(150)
turtle.pendown()


'''turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()'''
turtle.exitonclick()
