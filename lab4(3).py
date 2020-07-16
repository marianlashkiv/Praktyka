# Запитуємо текст у користувача
text = input("Введіть ваш текст:\n").lower()

# Множина голосних літер
a = {'a', 'e', 'i', 'o', 'u', 'y'}

# Шукаємо літери які є у множині та тексті
letters = []
for letter in text:
    if letter in a and letter not in letters:
        letters.append(letter)

# Сортуємо в алфавітному порядку
letters = sorted(letters)

# Виводимо літери
print("\n")
for letter in letters:
    print(f"У тексті є голосна літера - {letter}")
