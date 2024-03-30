studentList = ["Вася", "Петя"]
studentGrades = {"Вася": [], "Петя": []}

while True:
    answer = int(input("выберите действие\n"
                       "1-добавить студента\n"
                       "2-удалить студента (по номеру)\n"
                       "3-удалить студента (по имени)\n"
                       "4-посмотреть весь список студентов\n"
                       "5-добавить оценку студенту\n"
                       "6-посмотреть оценки студента\n"
                       "0-выйти из программы\n"))
    if answer not in [1, 2, 3, 4, 5, 6, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента: ")
        studentList.append(newStudent)
        studentGrades[newStudent] = []
    elif answer == 2:
        delNumber = int(input("введите номер студента для удаления: "))
        if delNumber < len(studentList):
            del studentGrades[studentList[delNumber]]
            studentList.pop(delNumber)
        else:
            print("Неверный номер студента.")
    elif answer == 3:
        delStudent = input("введите имя студента для удаления: ")
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
    elif answer == 0:
        break