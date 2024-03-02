import turtle

# Настройка черепашки
turtle.speed(0)  # Установить максимальную скорость
turtle.hideturtle()  # Скрыть черепашку

# Нарисовать стены дома
turtle.color("brown")
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(150)
turtle.end_fill()

# Нарисовать крышу дома
turtle.color("red")
turtle.begin_fill()
turtle.left(135)
turtle.forward(141.42)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(141.42)
turtle.end_fill()

# Завершение рисования
turtle.done()