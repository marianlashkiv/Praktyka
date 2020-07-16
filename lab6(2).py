import lab6_str_func

list_of_elements = [1, 8, 9, 2, 1, 5, 6, 9, 4, 5]

value = 5

sequence = [9, 2]

print(f"Список елементів - {list_of_elements}")

print("\n")
print("--Виберіть дію--")
while True:
    choose = input("\t1 - Сортування;\n\t2 - Пошук елементу за значенням;\n\t3 - Пошук послідовності елементів;\
\n\t4 - Пошук перших п’яти мінімальних елементів;\n\t5 - Пошук перших п’яти максимальних елементів;\
\n\t6 - Пошук середнього арифметичного;\n\t7 - Отримати список без повторень.\nВаш вибір - ")
    if choose == '1':
        print("\n")
        print(lab6_str_func.sort_list(list_of_elements))
    elif choose == '2':
        print("\n")
        print(lab6_str_func.find_element(list_of_elements, value))
    elif choose == '3':
        print("\n")
        print(lab6_str_func.find_sequence(list_of_elements, sequence))
    elif choose == '4':
        print("\n")
        print(lab6_str_func.find_5_min(list_of_elements))
    elif choose == '5':
        print("\n")
        print(lab6_str_func.find_5_max(list_of_elements))
    elif choose == '6':
        print("\n")
        print(lab6_str_func.get_avg(list_of_elements))
    elif choose == '7':
        print("\n")
        print(lab6_str_func.distinct_elements(list_of_elements))
