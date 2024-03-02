import turtle

def draw_star(n):
    """Рисует звезду с n концами."""

    # Установить начальное положение и направление
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.setheading(0)

    # Нарисовать лучи звезды
    for i in range(n):
        turtle.forward(200)
        turtle.left(180 - 180 / n)

# Нарисовать звезду с 5 концами
draw_star(5)

# Нарисовать звезду с 7 концами
draw_star(7)

# Нарисовать звезду с 9 концами
draw_star(9)

turtle.done()