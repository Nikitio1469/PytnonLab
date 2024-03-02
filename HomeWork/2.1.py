# Запрос ввода у пользователя
miles = input("Введите количество миль: ")

# Преобразование ввода в число
miles_num = int(miles)

# Перевод миль в километры
kilometers = miles_num * 1.60934

# Вывод результата
print(f"{miles_num} миль = {kilometers:.2f} километров")