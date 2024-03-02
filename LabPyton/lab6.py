import turtle

# Настройка черепашки
turtle.speed(0)
turtle.hideturtle()

# Получение ввода от пользователя
num_sides = int(input("Введите количество углов (3-5): "))

# Проверка ввода
if num_sides < 3 or num_sides > 5:
    print("Количество углов должно быть от 3 до 5.")
else:
    # Угол поворота для данной фигуры
    angle = 135

    # Рисование фигуры
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(num_sides):
        turtle.forward(100)
        turtle.left(angle)
    turtle.end_fill()

    # Отображение рисунка
    turtle.done()