import turtle

i = 0
x = -200
y = 200
turtle.penup()
turtle.goto(x, y)

while i <= 5:
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(x, y - 100 * (i + 1)) 
    i += 1

turtle.penup()
turtle.right(90)
turtle.goto(x, y)
i = 0
while i <= 5:
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(x + 100 * (i + 1), y) 
    i += 1

turtle.exitonclick()