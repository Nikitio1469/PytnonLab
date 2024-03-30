studentList = ["Вася", "Петя"]
while True:
    answer = int(input("выберите действие\n"
                       "1-добавить студента\n"
                       "2-удалить студента (по номеру)\n"
                       "3-удалить студента (по имени)\n"
                       "4-посмотреть весь список студентов\n"
                       "0-выйти из программы\n"))
    if answer not in [1, 2, 3, 4, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента: ")
        studentList.append(newStudent)
    elif answer == 2:
        delNumber = int(input("введите номер студента для удаления: "))
        if delNumber < len(studentList):
            studentList.pop(delNumber)
        else:
            print("Неверный номер студента.")
    elif answer == 3:
        delStudent = input("введите имя студента для удаления: ")
        if delStudent in studentList:
            studentList.remove(delStudent)
            print("Студент", delStudent, "удален из списка.")
        else:
            print("Студента", delStudent, "нет в списке.")
    elif answer == 4:
        print(studentList)
    elif answer == 0:
        break