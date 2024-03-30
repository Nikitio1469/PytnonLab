# Запрос текста и слова от пользователя
text = input("Введите текст:")
word = input("Введите слово для поиска:")

text_lower = text.lower()
word_lower = word.lower()

if word_lower in text_lower:
    position = text_lower.find(word_lower)
    print(f"Слово '{word}' найдено в тексте в позиции: {position}")
else:
    print(f"Слово '{word}' не найдено в тексте.")