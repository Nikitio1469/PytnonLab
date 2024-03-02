# Запрос ввода суммы в рублях у пользователя
rubles = int(input("Введите сумму в рублях: "))

# Запрос ввода валюты у пользователя
currency = input("В какую валюту перевести (доллары, евро или юани): ")

# Перевод рублей в соответствующую валюту по курсу
if currency == "доллары":
    rate = 75  # Курс доллара к рублю
    converted_amount = rubles / rate
    print(f"{rubles} рублей = {converted_amount:.2f} долларов")
elif currency == "евро":
    rate = 85  # Курс евро к рублю
    converted_amount = rubles / rate
    print(f"{rubles} рублей = {converted_amount:.2f} евро")
elif currency == "юани":
    rate = 10  # Курс юаня к рублю
    converted_amount = rubles / rate
    print(f"{rubles} рублей = {converted_amount:.2f} юаней")
else:
    print("Неизвестная валюта.")