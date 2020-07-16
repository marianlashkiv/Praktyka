import random

n = len(input("Введіть ваше імя - "))

m = len(input("Введіть ваше прізвище - "))

# Генеруємо масив
array = []
for i in range(m):
    array.append([])
    for j in range(n):
        array[i].append(random.uniform(0, 1))

# Виводимо рядки масиву
print(f"\n--Масив--")
for i in array:
    print(i)

# Генеруємо список сум стовпців
columns_sum = []
for a in range(n):
    sum_of_column = 0
    for i in array:
        sum_of_column += i[a]
    columns_sum.append(sum_of_column)

# Виводимо список сум стовпців
print(f"\n--Cуми стовпців--")
for i in range(len(columns_sum)):
    print(f"Сума стовпця {i+1} - {columns_sum[i]}")



