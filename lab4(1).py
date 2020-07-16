# Запитуємо речення у користувача
text = input("Введіть ваше речення:\n")

# Визначаємо слова
words = text.split()

# Виводимо слова з речення
print("\n-Список слів-")
print(str(words) + "\n")
for i in range(len(words)):
    print(f"Слово {i+1} - {words[i]}")
