# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги (не пустая строка).
        :param author: Автор книги (не пустая строка).
        :param pages: Количество страниц (должно быть > 0).
        :raises ValueError: Если название/автор пустые или страниц <= 0.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.title
        '1984'
        """
        if not title or not author:
            raise ValueError("Название и автор не могут быть пустыми.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int = 10) -> str:
        """
        Чтение книги. Возвращает сообщение о прочитанных страницах.

        :param pages_read: Сколько страниц прочитано (по умолчанию 10).
        :return: Сообщение о прочтении.
        :raises ValueError: Если pages_read <= 0 или > общего числа страниц.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(50)
        'Прочитано 50 из 328 страниц.'
        """
        if pages_read <= 0 or pages_read > self.pages:
            raise ValueError("Некорректное количество страниц.")
        return f"Прочитано {pages_read} из {self.pages} страниц."

    def get_reading_time(self, speed: int = 30) -> float:
        """
        Рассчитывает время чтения книги (в часах).

        :param speed: Скорость чтения (страниц в час, по умолчанию 30).
        :return: Время в часах.
        :raises ValueError: Если speed <= 0.

        >>> book = Book("1984", "George Orwell", 300)
        >>> book.get_reading_time(50)
        6.0
        """
        if speed <= 0:
            raise ValueError("Скорость чтения должна быть положительной.")
        return self.pages / speed
# TODO: описать ещё класс
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        """
        Инициализация банковского счёта.

        :param owner: Владелец счёта.
        :param balance: Начальный баланс (не может быть отрицательным).
        :raises ValueError: Если balance < 0.

        >>> acc = BankAccount("Alice", 1000.0)
        >>> acc.owner
        'Alice'
        """
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Внесение денег на счёт.

        :param amount: Сумма для внесения (должна быть > 0).
        :raises ValueError: Если amount <= 0.

        >>> acc = BankAccount("Alice")
        >>> acc.deposit(500.0)
        >>> acc.balance
        500.0
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счёта. Возвращает сумму снятия.

        :param amount: Сумма для снятия (должна быть > 0 и <= баланса).
        :return: Снятая сумма.
        :raises ValueError: Если amount <= 0 или > баланса.

        >>> acc = BankAccount("Bob", 1000.0)
        >>> acc.withdraw(200.0)
        200.0
        """
        if amount <= 0 or amount > self.balance:
            raise ValueError("Некорректная сумма для снятия.")
        self.balance -= amount
        return amount
# TODO: и ещё один
class TemperatureSensor:
    def __init__(self, location: str, current_temp: float = 20.0):
        """
        Инициализация датчика температуры.

        :param location: Местоположение датчика.
        :param current_temp: Текущая температура (по умолчанию 20.0°C).
        :raises ValueError: Если температура вне допустимого диапазона.

        >>> sensor = TemperatureSensor("Кухня", 25.5)
        >>> sensor.location
        'Кухня'
        """
        if current_temp < -273.15 or current_temp > 1000:
            raise ValueError("Температура вне допустимого диапазона.")
        self.location = location
        self.current_temp = current_temp

    def update_temp(self, new_temp: float) -> None:
        """
        Обновляет текущую температуру.

        :param new_temp: Новая температура.
        :raises ValueError: Если температура вне допустимого диапазона.

        >>> sensor = TemperatureSensor("Гостиная")
        >>> sensor.update_temp(22.0)
        >>> sensor.current_temp
        22.0
        """
        if new_temp < -273.15 or new_temp > 1000:
            raise ValueError("Температура вне допустимого диапазона.")
        self.current_temp = new_temp

    def is_freezing(self) -> bool:
        """
        Проверяет, замерзает ли вода (t <= 0°C).

        :return: True, если температура <= 0°C.

        >>> sensor = TemperatureSensor("Балкон", -5.0)
        >>> sensor.is_freezing()
        True
        """
        return self.current_temp <= 0.0