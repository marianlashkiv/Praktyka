import sqlite3

connect = sqlite3.connect("lab10.db")
cursor = connect.cursor()


def create_table():
    """Видаляємо таблицю з БД якщо вона вже створена та створюємо знову"""
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("CREATE TABLE books (num int PRIMARY KEY, author varchar(255), name varchar(255),\
    publisher varchar(255), genre varchar(255), year int)")


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

    def write_to_db(self, num):
        """
        Записуємо дані про книгу в БД
        :param num: номер книги
        :return: повідомлення про вдалість/невдалість операції
        """
        if num in self.books:
            query = "INSERT INTO books VALUES(?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (num, self.books[num]['author'], self.books[num]['name'], self.books[num]['publisher'],
                                   self.books[num]['genre'], self.books[num]['year']))
            connect.commit()
            return f"Книга -{num}- записана в БД!"
        else:
            return f"Книгу -{num}- не знайдено("

    def del_from_db(self, num):
        """
        Видаляємо запис з БД
        :param num: номер книги
        :return: повідомлення про виконання операції
        """
        query = "DELETE FROM books WHERE num=?"
        cursor.execute(query, (num,))
        connect.commit()
        return f"Книга -{num}- видалена з БД!"


def get_records(value):
    """
    Шукаємо записи в БД за вказаним значення року видання
    :param value: рік видання книги
    :return: список записів
    """
    query = "SELECT * FROM books WHERE year=?"
    cursor.execute(query, (value,))
    return cursor.fetchall()


books = Library()
create_table()

# Додаємо книги для перевірки
books.add_book(1, {'author': 'a', 'name': 'a', 'publisher': 'a', 'genre': 'a', 'year': 2011})
books.add_book(2, {'author': 'b', 'name': 'b', 'publisher': 'b', 'genre': 'b', 'year': 2015})

print("""Вас вітає \"Домашня бібліотека!\"""")

while True:
    choose = input("Виберіть Вашу дію:\n\t1 - Додати книгу\n\t2 - Видалити книгу\n\t3 - Отримати інформацію про книгу\
    \n\t4 - Знайти книгу за параметром\n\t5 - Записати книгу в БД\n\t6 - Видалити книгу з БД\n\t7 - Записи в БД за роком\
    \nВаш вибір - ")

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

    # Запитуємо номер книги та записуємо дані про цю книгу в БД
    elif choose == '5':
        num = int(input("\n\nВведіть номер книги - "))
        print(books.write_to_db(num))

    # Запитуємо номер книги та видаляємо дані про цю книгу з БД
    elif choose == '6':
        num = int(input("\n\nВведіть номер книги - "))
        print(books.del_from_db(num))

    elif choose == '7':
        year = int(input("\n\nВведіть рік видання книги - "))
        for record in get_records(year):
            print(record)

    # Виводимо повідомлення у разі некоректного вводу номеру команди
    else:
        print("\n\nПомилкова команда")
