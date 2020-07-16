class Library:

    def __init__(self):
        """ Конструктор
        """
        self.books = {}

    def add_book(self, num, data):
        """
        Додаємо книгу
        :param num: номер книги
        :param data: дані про книгу
        :return: повідомлення про додання книги
        """
        self.books[num] = data
        return f"Книга -{num}- додана!"

    def del_book(self, num):
        """
        Видаляємо книгу за вказаним номером
        :param num: номер книги
        :return: повідомлення про вдалість/невдалість операції
        """
        if num in self.books:
            del self.books[num]
            return f"Книга -{num}- видалена!"
        else:
            return f"Книгу -{num}- не знайдено("

    def get_info(self, num):
        """
        Отримуємо інформацію про книгу за вказаним номером
        :param num: номер книги
        :return: дані про книгу
        """
        if num in self.books:
            return self.books[num]


    def get_all(self):
        """
        Отримуємо всі дані про книги
        :return: дані книг
        """
        return self.books.items()


books = Library()


# Додаємо книги для перевірки
books.add_book(1, {'author': 'a', 'name': 'a', 'publisher': 'a', 'genre': 'a', 'year': 1})
books.add_book(2, {'author': 'b', 'name': 'b', 'publisher': 'b', 'genre': 'b', 'year': 2})
print("""Вас вітає \"Домашня бібліотека!\"""")

while True:
    choose = input("Виберіть Вашу дію:\n\t1 - Додати книгу\n\t2 - Видалити книгу\n\t3 - Отримати інформацію про книгу\
    \n\t4 - Знайти книгу за параметром\nВаш вибір - ")

    # Якщо вибрали команду 1, то запитуємо дані про кинигу та додаємо її до бібліотеки
    if choose == '1':
        num = int(input("\n\nВведіть номер книги - "))
        author = input("Введіть автора книги - ")
        name = input("Введіть назву книги - ")
        publisher = input("Введіть видавництво книги - ")
        genre = input("Введіть жанр книги - ")
        year = input("Введіть рік видання книги - ")
        print(
            books.add_book(num, {'author': author, 'name': name, 'publisher': publisher, 'genre': genre, 'year': year}))

    # Запитуємо номер книги та видаляємо її
    elif choose == '2':
        num = int(input("\n\nВведіть номер книги - "))
        print(books.del_book(num))

    # Запитуємо номер книги та вивдимо всю інформацію про неї
    elif choose == '3':
        num = int(input("\n\nВведіть номер книги - "))
        try:
            data = books.get_info(num)
            print(f"Інформація про книгу -{num}-")
            for key in data.items():
                print(f"{str(key[0]).title()} - {key[1]}")
        except:
            print(f"Книгу -{num}- не знайдено(")

    # Запитуємо параметр та його значення за якими шукатимемо книги та виводиму інформацію
    elif choose == '4':
        list_of_param = ['author', 'name', 'publisher', 'genre', 'year']
        param = int(input("Виберіть параметр за яким потрібно шукати:\n\t1 - Автор\n\t2 - Назва\n\t3 - Видавництво\
\n\t4 - Жанр\n\t5 - Рік\nВаш вибір - ")) - 1
        param = list_of_param[param]
        value = input("Введіть значення параметру - ")
        all_books = books.get_all()
        selected_books = []
        for num in all_books:
            data = num[1]
            if str(data[param]) == value:
                selected_books.append(num)
        print(f"Список книг з вибірки - {selected_books}")

    # Виводимо повідомлення у разі некоректного вводу номеру команди
    else:
        print("\n\nПомилкова команда")
