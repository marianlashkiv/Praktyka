import random

# Запитуємо та виводимо значення змінної n
n = int(input("Введіть значення n - "))
print(f"n={n}")

# Генеруємо список
list_of_elements = []
for i in range(n):
    list_of_elements.append(random.randint(-10, 10))

print(f"Cписок - {list_of_elements}")

slice_of_abs_elements = []

# Генеруємо слайс
if 0 in list_of_elements:
    index = list_of_elements.index(0)
    for i in list_of_elements[index:]:
        slice_of_abs_elements.append(abs(i))
    print(f"Сума модулів елементів, розміщених після першого елементу - {sum(slice_of_abs_elements)}")
else:
    print("У списку немає нульового елементу")
