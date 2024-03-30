import random

studentList = ["Вася", "Петя"]
studentGrades = {"Вася": [], "Петя": []}

# Добавление еще 5 имен и оценок
for _ in range(3):
    newStudent = input("Введите имя студента: ")
    studentList.append(newStudent)
    studentGrades[newStudent] = []

while True:
    answer = int(input("выберите действие\n"
                       "1-добавить студента\n"
                       "2-удалить студента (по номеру)\n"
                       "3-удалить студента (по имени)\n"
                       "4-посмотреть весь список студентов\n"
                       "5-добавить оценку студенту\n"
                       "6-посмотреть оценки студента\n"
                       "7-посмотреть список по оценкам\n"
                       "8-добавить рандомные оценки студентам\n"
                       "0-выйти из программы\n"))

    if answer not in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        print("такой команды нет")
        continue

    elif answer == 8:
        for student in studentGrades:
            random_grades = [random.randint(1, 5) for _ in range(3)]  # Генерация 3 рандомных оценок от 1 до 10 для каждого студента
            studentGrades[student] = random_grades
    
    elif answer == 1:
        newStudent = input("Введите имя студента: ")
        studentList.append(newStudent)
        studentGrades[newStudent] = []
    
    elif answer == 2:
        delNumber = int(input("Введите номер студента для удаления: "))
        if delNumber < len(studentList):
            del studentGrades[studentList[delNumber]]
            studentList.pop(delNumber)
        else:
            print("Неверный номер студента.")
    
    elif answer == 3:
        delStudent = input("Введите имя студента для удаления: ")
        if delStudent in studentList:
            del studentGrades[delStudent]
            studentList.remove(delStudent)
            print("Студент", delStudent, "удален из списка.")
        else:
            print("Студента", delStudent, "нет в списке.")
    
    elif answer == 4:
        print(studentList)
    
    elif answer == 5:
        studentName = input("Введите имя студента: ")
        if studentName in studentList:
            grade = float(input("Введите оценку студента {}: ".format(studentName)))
            studentGrades[studentName].append(grade)
        else:
            print("Студента", studentName, "нет в списке.")
    
    elif answer == 6:
        studentName = input("Введите имя студента, чьи оценки вы хотите посмотреть: ")
        if studentName in studentList:
            print("Оценки студента {}: {}".format(studentName, studentGrades[studentName]))
        else:
            print("Студента", studentName, "нет в списке.")

    elif answer == 7:
        print("Список по оценкам:")
        for student in studentGrades:
            print(student, ": ", studentGrades[student])
    
    elif answer == 0:
        break
