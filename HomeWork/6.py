import turtle

def draw_star(n):
    """Рисует звезду с n концами."""

    # Установить начальное положение и направление
    turtle.penup()
    turtle.goto(0, 0)  # Изменено положение начала рисования звезды
    turtle.pendown()

    # Нарисовать лучи звезды
    for i in range(n):
        turtle.forward(200)
        turtle.left(180 - 180 / n)

# Нарисовать звезду с 9 концами
draw_star(9)


turtle.done()