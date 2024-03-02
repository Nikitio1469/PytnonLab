import turtle

# Настройка черепашки
turtle.speed(0)
turtle.hideturtle()

# Рисование нижней окружности
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Рисование средней окружности
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# Рисование верхней окружности
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# Рисование глаз
turtle.penup()
turtle.goto(-15, 40)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(15, 40)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# Рисование носа
turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# Рисование рта
turtle.penup()
turtle.goto(-10, 20)
turtle.pendown()
turtle.setheading(-90)
turtle.forward(20)

# Рисование рук
turtle.penup()
turtle.goto(-30, 0)
turtle.pendown()
turtle.setheading(0)
turtle.forward(60)

turtle.penup()
turtle.goto(30, 0)
turtle.pendown()
turtle.setheading(0)
turtle.forward(60)

# Рисование пуговиц
turtle.penup()
turtle.goto(0, -10)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# Отображение рисунка
turtle.done()