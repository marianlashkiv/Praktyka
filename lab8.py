class Transport:

    def __init__(self, price, speed, year):
        """
        Конструктор
        """
        self.__price = price
        self.__speed = speed
        self.__year = year

    def get_price(self):
        """
        Повертаємо захищений атрибут __price
        """
        return self.__price

    def get_speed(self):
        """
        Повертаємо захищений атрибут __speed
        """
        return self.__speed

    def get_year(self):
        """
        Повертаємо захищений атрибут __year
        """
        return self.__year

    def set_price(self, price):
        """
        Змінюємо захищений атрибут __price
        """
        self.__price = price

    def set_speed(self, speed):
        """
        Змінюємо захищений атрибут __speed
        """
        self.__speed = speed

    def set_year(self, year):
        """
        Змінюємо захищений атрибут __year
        """
        self.__year = year


class Boat(Transport):

    def __init__(self, price, speed, year, count_of_passengers, port):
        """
        Конструктор
        """
        super().__init__(price, speed, year)
        self.count_of_passengers = count_of_passengers
        self.port = port


class Plane(Transport):

    def __init__(self, price, speed, year, count_of_passengers, height):
        """
        Конструктор
        """
        super().__init__(price, speed, year)
        self.count_of_passengers = count_of_passengers
        self.height = height


class Car(Transport):

    def __init__(self, price, speed, year, count_of_passengers, engine):
        """
        Конструктор
        """
        super().__init__(price, speed, year)
        self.count_of_passengers = count_of_passengers
        self.engine = engine


aurora = Boat(40000, 50, 2019, 4, 'Palm-Harbor')
corner = Plane(7000, 80, 2007, 2, 1500)
toyota = Car(14000, 240, 2014, 5, 3.5)


while True:
    choose = input("Виберіть Вашу дію:\n\t1 - Змінити ціну обєкту\n\t2 - Змінити швидкість обєкту\n\t3 - Змінити рік обєкту\
    \n\t4 - Вивести усі атрибути обєкту\nВаш вибір - ")
    if choose == '1':
        select = input("Виберіть обєкт:\n\t1 - Автомобіль Toyota\n\t2 - Літак Corner\n\t3 - Корабель Aurora\nВаш вибір - ")
        if select == '1':
            price = float(input("Введіть нову ціну - "))
            toyota.set_price(price)
            print("Ціну змінено!")
        elif select == '2':
            price = float(input("Введіть нову ціну - "))
            corner.set_price(price)
            print("Ціну змінено!")
        elif select == '3':
            price = float(input("Введіть нову ціну - "))
            aurora.set_price(price)
            print("Ціну змінено!")
    elif choose == '2':
        select = input("Виберіть обєкт:\n\t1 - Автомобіль Toyota\n\t2 - Літак Corner\n\t3 - Корабель Aurora\nВаш вибір - ")
        if select == '1':
            speed = float(input("Введіть нову швидкість - "))
            toyota.set_speed(speed)
            print("Швидкість змінено!")
        elif select == '2':
            speed = float(input("Введіть нову швидкість - "))
            corner.set_speed(speed)
            print("Швидкість змінено!")
        elif select == '3':
            speed = float(input("Введіть нову швидкість - "))
            aurora.set_speed(speed)
            print("Швидкість змінено!")
    elif choose == '3':
        select = input("Виберіть обєкт:\n\t1 - Автомобіль Toyota\n\t2 - Літак Corner\n\t3 - Корабель Aurora\nВаш вибір - ")
        if select == '1':
            year = int(input("Введіть новий рік - "))
            toyota.set_year(year)
            print("Рік змінено!")
        elif select == '2':
            year = int(input("Введіть новий рік - "))
            corner.set_year(year)
            print("Рік змінено!")
        elif select == '3':
            year = int(input("Введіть новий рік - "))
            aurora.set_year(year)
            print("Рік змінено!")
    elif choose == '4':
        select = input("Виберіть обєкт:\n\t1 - Автомобіль Toyota\n\t2 - Літак Corner\n\t3 - Корабель Aurora\nВаш вибір - ")
        if select == '1':
            print(f"- Автомобіль Toyota -\n\tЦіна - {toyota.get_price()}\n\tШвидкість - {toyota.get_speed()}\
\n\tРік - {toyota.get_year()}\n\tКількість пасажирів - {toyota.count_of_passengers()}\n\tДвигун - {toyota.engine()}")
        elif select == '2':
            print(f"- Літак Corner -\n\tЦіна - {corner.get_price()}\n\tШвидкість - {corner.get_speed()}\
            \n\tРік - {corner.get_year()}\n\tКількість пасажирів - {corner.count_of_passengers()}\n\tВисота - {corner.height()}")
        elif select == '3':
            print(f"- Корабель Aurora -\n\tЦіна - {aurora.get_price()}\n\tШвидкість - {aurora.get_speed()}\
            \n\tРік - {aurora.get_year()}\n\tКількість пасажирів - {aurora.count_of_passengers}\n\tПорт - {aurora.port}")
