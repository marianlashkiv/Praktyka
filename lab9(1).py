import os


def get_all_files():
    """
    Усі файли в директорії
    :return: назви файли
    """
    files_name = []
    for file in os.listdir():
        files_name.append(file)
    return files_name


def exists_file(file_name):
    """
    Пошук в директорії за назвою файлу
    :param file_name: назва файлу
    :return: True/False
    """
    exists = f"Файл -{file_name}- не знайдено"
    for file in os.listdir():
        if file == file_name:
            exists = f"Файл -{file_name}- знайдено"
            break
    return exists


def read_file():
    """
    Записує отримані з файлу дані у список
    """
    file_with_name = open('names.txt', 'r', encoding='utf-8')
    file_with_mark = open('marks.txt', 'r', encoding='utf-8')
    names = []
    marks = []
    for line in file_with_name:
        names.append(line.replace('\n', ''))
    for line in file_with_mark:
        marks.append(line.replace('\n', ''))
    file_with_name.close()
    file_with_mark.close()
    return names, marks


def sort_files(file_a, file_b):
    """
    Сортує дані
    :param file_a: колонка 1
    :param file_b: колонка 2
    :return: Сортований список
    """
    sorted_files = sorted(zip(file_b, file_a))
    return sorted_files


def search_data(file_a, file_b, param):
    """
    Пошук рядку за параметром
    :param file_a: колонка 1
    :param file_b: колонка 2
    :param param: параметр
    :return: True/False
    """
    zip_files = zip(file_a, file_b)
    for i in zip_files:
        if param in i:
            return f"Параметр -{param}- знайдено у рядку: {i}"
            break
    return f"Параметр -{param}- не знайдено"


def write_row(name, mark):
    """
    Дозаписуємо дані у файли
    :param name: імя
    :param mark: оцінка
    """
    log_file = os.path.join('names.txt')
    with open(log_file, 'a', encoding='utf 8') as log:
        print(name, file=log)
    log_file = os.path.join('marks.txt')
    with open(log_file, 'a', encoding='utf 8') as log:
        print(mark, file=log)
    return f"Дані -- {name}-{mark} -- успішно записано!"


if __name__ == "__main__":
    file_with_names, file_with_marks = read_file()
    while True:
        print("\n--Виберіть дію--")
        choose = input("\t1 - Усі файли в директорії;\n\t2 - Пошук в директорії за назвою файлу;\n\t3 - Сортувати за балами;\
\n\t4 - Пошук рядку за параметром;\n\t5 - Додати дані у файли.\nВаш вибір - ")
        if choose == '1':
            print("\n")
            for file in get_all_files():
                print(file)
        elif choose == '2':
            print("\n")
            name = input("Введіть назву файлу - ")
            print(exists_file(name))
        elif choose == '3':
            print("\n")
            for row in sort_files(file_with_names, file_with_marks):
                print(row)
        elif choose == '4':
            print("\n")
            value = input("Введіть параметр - ")
            print(search_data(file_with_names, file_with_marks, value))
        elif choose == '5':
            print("\n")
            added_name = input("Введіть імя яке бажаєте додати - ")
            added_mark = input("Введіть середній бал який бажаєте додати - ")
            print(write_row(added_name, added_mark))
            file_with_names, file_with_marks = read_file()
        else:
            continue
