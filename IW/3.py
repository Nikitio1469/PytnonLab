m = int(input("Введите массу конфет в граммах: "))

if m > 2000:
    price_per_kg = 200
else:
    price_per_kg = 250

price_per_gram = price_per_kg / 1000
price = m * price_per_gram

print(f"Цена за 1 кг конфет составляет {price_per_kg} рублей")
print(f"Цена конфет введенной массы {m} грамм составляет {price:.2f} рублей")
