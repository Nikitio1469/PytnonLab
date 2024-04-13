import turtle

t = turtle.Turtle()
t.speed(0)
t.color("black")

n = 19
angle = 5
cur_size = 4

t.width(3) 

for _ in range(2): 
    for i in range(n):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(angle * i)
        t.penup()
        t.backward(cur_size / 2)
        t.right(90)
        t.forward(cur_size / 2)
        t.left(90)
        t.pendown()
        for _ in range(4):
            t.forward(cur_size)
            t.left(90)
        cur_size += 5

turtle.done()