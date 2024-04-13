import random
length = int(input("Введите длину пароля: "))
password = ''.join(random.choice('0123456789') 
for i in range(length))
print(f"Сгенерированный пароль: {password}")