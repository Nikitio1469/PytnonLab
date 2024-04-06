import random

timeList = ["Сегодня", "Завтра", "Очень скоро"]
eventList = ["вы встретите", "с вами случится", "вы найдёте"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]

while True:
    zodiac_sign = input("Введите знак Зодиака: ")

    # Проверяем правильность введённого знака Зодиака
    if zodiac_sign.lower() not in ['овен', 'телец', 'близнецы', 'рак', 'лев', 'дева', 'весы', 'скорпион', 'стрелец', 'козерог', 'водолей', 'рыбы']:
        print("Пожалуйста, введите правильный знак Зодиака.")
        continue

    time = timeList[random.randint(0, len(timeList) - 1)]
    event = eventList[random.randint(0, len(eventList) - 1)]
    object = objectList[random.randint(0, len(objectList) - 1)]

    print(time + " " + event + " " + object)

    response = input("Хотите получить ещё одно предсказание? (да/нет): ")
    if response.lower() != "да":
        break

print("Приходите ещё за новыми предсказаниями!")