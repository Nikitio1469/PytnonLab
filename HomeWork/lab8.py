import random

print("добро пожаловать в игру камень ножницы бумага ящерица спок!")
playerScore = 0
botScore = 0

for i in range(5):
    answer = input("Что выберешь?\n").lower()
    if answer.find("камень") != -1:
        answer = "к"
    elif answer.find("ножницы") != -1:
        answer = "н"
    elif answer.find("бумага") != -1 or answer.find("бумагу") != -1:
        answer = "б"

    elif answer.find("ящерицу") != -1 or answer.find("ящерица") != -1:
       answer = "я"
    elif answer.find("спок") != -1:
       answer = "с"
    
    botAnswer = random.choice(["камень", "ножницы", "бумагу", "ящерицу", "спок"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]
    
    if answer == botAnswer:
        print("ничья!")
    elif (answer == "к" and botAnswer == "н") or (answer == "н" and botAnswer == "б") or \
         (answer == "б" and botAnswer == "к") or (answer == "к" and botAnswer == "я") or \
         (answer == "н" and botAnswer == "я") or (answer == "я" and botAnswer == "с") or \
         (answer == "я" and botAnswer == "б") or (answer == "с" and botAnswer == "к") or \
         (answer == "с" and botAnswer == "н"):
        print("ты победил!")
        playerScore += 1
    else:
        print("я победил!")
        botScore += 1

if playerScore == botScore:
    print("ничья по итогам пяти раундов!")
elif playerScore > botScore:
    print("ты победил по итогам пяти раундов")
else: 
    print("я победил по итогам пяти раундов")