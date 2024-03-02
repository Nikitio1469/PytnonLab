# Список вопросов и ответов
questions = [
    ("Столица Англии?", "Лондон"),
    ("Самое большое озеро в мире?", "Байкал"),
    ("Самый теплый океан в мире?", "Индийский океан"),
    ("Автор книги «Таинственный остров»?", "Жюль Верн"),
    ("Сколько планет в «Солнечной системе»?, "8").
    
]

# Получение ответа от пользователя
def get_answer(question):
    answer = input(question + " ")
    return answer

# Проверка ответа
def check_answer(question, answer):
    correct_answer = questions[question][1]
    return answer == correct_answer

# Основной цикл викторины
def main():
    score = 0
    for i, question in enumerate(questions):
        answer = get_answer(question[0])
        if check_answer(i, answer):
            score += 1
    print("Ваш счет:", score, "/", len(questions))

# Запуск викторины
if __name__ == "__main__":
    main()