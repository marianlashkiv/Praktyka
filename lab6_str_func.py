def sort_list(unsorted_list):
    """
    Сортування
    :param unsorted_list: несортований список
    :return: сортований список
    """
    return f"Сортований список{sorted(unsorted_list)}"


def find_element(list_of_elements, find_element):
    """
    Пошук елементу за значенням
    :param list_of_elements: список елементів
    :param find_element: значення елементу
    :return: True/False
    """
    if find_element in list_of_elements:
        return f"Елемент -{find_element}- знайдено у списку"
    else:
        return f"Елемент -{find_element}- незнайдено у списку"


def find_sequence(list_of_elements, sequence):
    """
    Пошук послідовності елементів
    :param list_of_elements: список елементів
    :param sequence: шукану послідовність
    :return: True/False
    """
    if sequence[0] in list_of_elements:
        start_index = list_of_elements.index(sequence[0])
        for i in sequence[1:]:
            start_index += 1
            if i == list_of_elements[start_index]:
                continue
            else:
                return f"Послідовність -{sequence}- незнайдено у списку"
        return f"Послідовність -{sequence}- знайдено у списку"
    else:
        return f"Послідовність -{sequence}- незнайдено у списку"


def find_5_min(list_of_elements):
    """
    Пошук перших п’яти мінімальних елементів
    :param list_of_elements: список елементів
    """
    if len(list_of_elements) < 5:
        return "Список має менше пяти елементів!"
    else:
        sorted_list = sorted(list_of_elements.copy())
        return sorted_list[:5]


def find_5_max(list_of_elements):
    """
    Пошук перших п’яти максимальних елементів
    :param list_of_elements: список елементів
    """
    if len(list_of_elements) < 5:
        return "Список має менше пяти елементів!"
    else:
        sorted_list = sorted(list_of_elements.copy())
        max_5 = sorted_list[-5:].copy()
        max_5.reverse()
        return max_5


def get_avg(list_of_elements):
    """
    Пошук середнього арифметичного
    :param list_of_elements: список елементів
    :return: середнє арифметичне
    """
    return sum(list_of_elements)/len(list_of_elements)


def distinct_elements(list_of_elements):
    """
    Повернення списку, що сформований з початкового списку, але не містить повторів (залишається лише перший з однакових
    елементів)
    :param list_of_elements: список елементів
    :return: список без повторень
    """
    distinct_list = []
    for element in list_of_elements:
        if element not in distinct_list:
            distinct_list.append(element)
    return f"Список без повторень - {distinct_list}"
