from task import Book, BankAccount, TemperatureSensor

if __name__ == "__main__":
    try:
        # Инстанцируем все классы с корректными данными
        book = Book("1984", "George Orwell", 328)
        account = BankAccount("Alice", 1000.0)
        sensor = TemperatureSensor("Кухня", 25.5)

        # 1. Проверка класса Book с некорректными данными
        try:
            bad_book = Book("", "Author", 100)  # Пустое название
        except ValueError as e:
            print("Ошибка: неправильные данные")

    # 2. Проверка класса BankAccount с некорректными данными
        try:
            bad_account = BankAccount("Bob", -100.0)  # Отрицательный баланс
        except ValueError as e:
            print("Ошибка: неправильные данные")

    # 3. Проверка класса TemperatureSensor с некорректными данными
        try:
            bad_sensor = TemperatureSensor("Подвал", 1500.0)  # Слишком высокая температура
        except ValueError as e:
            print("Ошибка: неправильные данные")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")