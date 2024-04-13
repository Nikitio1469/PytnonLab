import turtle
 
radius = int(input("Введите радиус первого круга (синего): "))
 
screen = turtle.Screen()
screen.title("Пропорционально увеличивающиеся круги")
t = turtle.Turtle()
t.speed(5)

t.width(3) 
t.color("blue")
t.circle(radius)

for i in range(1, 4):
    radius += 20
    t.penup()
    t.sety(t.ycor() - 20)
    t.pendown()
    if i % 4 == 1:
        t.color("orange")
    elif i % 4 == 2:
        t.color("green")
    elif i % 4 == 3:
        t.color("red")
    else:
        t.color("blue")
    t.circle(radius)

screen.exitonclick()