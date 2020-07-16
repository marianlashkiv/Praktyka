# Запитуємо текст у користувача
text = input("Введіть ваш текст:\n")

# Множина голосних літер
a = {'a', 'e', 'i', 'o', 'u', 'y'}

# Множина приголосних літер
b = {'q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'}

# Множина цифр
nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

count_of_a = 0
count_of_b = 0
count_of_nums = 0

# Рахуємо кількість голосних, приголосних та цифр
for letter in text:
    if letter in a:
        count_of_a += 1
    elif letter in b:
        count_of_b += 1
    elif letter in nums:
        count_of_nums += 1

# Виводимо результати
if count_of_a > count_of_b:
    print("\nКількість голосних більша")
elif count_of_b > count_of_a:
    print("\nКількість приголосних більша")
else:
    print("\nКількість приголосних та голосних рівна")

print(f"\nКількість голосних - {count_of_a}")
print(f"Кількість приголосних - {count_of_b}")
print(f"Кількість цифр - {count_of_nums}")
