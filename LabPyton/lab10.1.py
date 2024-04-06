questions = ["Какая столица Англии?", "Сколько дней в году?", "Какого цвета листья весной?"]
rightAnswers = ["Лондон", "365", "Зеленого"]
rightCounter = 0
questionsCounter = 0

while questionsCounter < len(questions):
    answer = input(questions[questionsCounter])
    if answer.lower() == rightAnswers[questionsCounter].lower():
        print("Вы ответили верно!")
        rightCounter += 1
    else:
        print("Вы ответили не верно.")
    questionsCounter += 1

print(f"Вы набрали баллов: {rightCounter}")