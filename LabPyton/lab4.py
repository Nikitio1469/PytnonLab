age_ranges = [
    (0, 15, "Дети"),
    (16, 22, "Подростки"),
    (23, 30, "Молодые люди"),
    (31, 50, "Взрослые"),
    (51, 100, "Пожилые люди")
]

def get_age_range(age):
  """Возвращает возрастной диапазон для данного возраста."""
  for age_range in age_ranges:
    if age_range[0] <= age < age_range[1]:
      return age_range[2]
  return "Неизвестно"

# Примеры использования
print(get_age_range(10))  # Дети
print(get_age_range(25))  # Молодые люди
print(get_age_range(60))  # Пожилые люди
print(get_age_range(150))  # Неизвестно