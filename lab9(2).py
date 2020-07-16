def read_file(path):
    """
    Записує отримані з файлу дані у список
    """
    file = open(path, 'r', encoding='utf-8')
    data = []
    for line in file:
        data.append(line.replace('\n', ''))
    file.close()
    return data


def get_bigger(data):
    """
    Повертає дані про найдовший рядок
    :param data: список рядків
    """
    row_len = 0
    row_index = 0
    row_text = ""
    for row in range(len(data)):
        if len(data[row]) > row_len:
            row_len = len(data[row])
            row_index = row+1
            row_text = data[row]
    return row_len, row_index, row_text


file_data = read_file("lab9(2).txt")
row_len, row_index, row_text = get_bigger(file_data)

print(f"Довжина найдовшого рядка - {row_len}")
print(f"Індекс найдовшого рядка - {row_index}")
print(f"Текст найдовшого рядка - {row_text}")
