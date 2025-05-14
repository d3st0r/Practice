# TODO: описать базовый класс
class Animal:
    """Базовый класс для всех животных."""

    def __init__(self, name: str, age: int, habitat: str):
        """
        Инициализация животного.

        :param name: Название животного
        :param age: Возраст в годах
        :param habitat: Место обитания
        """
        self._name = name  # Инкапсулируем, так как имя не должно меняться после создания
        self.age = age
        self.habitat = habitat

    @property
    def name(self) -> str:
        """Возвращает имя животного (только для чтения)."""
        return self._name

    def make_sound(self) -> str:
        """
        Издает характерный звук.

        :return: Строка с описанием звука
        """
        return "Издает звук"

    def eat(self, food: str) -> str:
        """
        Процесс питания.

        :param food: Что ест животное
        :return: Строка с описанием процесса
        """
        return f"Ест {food}"

    def __str__(self) -> str:
        """Строковое представление животного."""
        return f"{self.name}, {self.age} лет, обитает в {self.habitat}"

    def __repr__(self) -> str:
        """Формальное представление для воссоздания объекта."""
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age}, habitat='{self.habitat}')"

# TODO: описать дочерний класс


class Cat(Animal):
    """Класс кошки, наследуется от Animal."""

    def __init__(self, name: str, age: int, habitat: str, breed: str, is_vaccinated: bool):
        """
        Инициализация кошки.

        :param breed: Порода кошки
        :param is_vaccinated: Привита ли кошка
        """
        super().__init__(name, age, habitat)
        self.breed = breed
        self.is_vaccinated = is_vaccinated

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound для кошки.
        Причина: кошки издают специфичный звук (мяуканье)
        """
        return "Мяукает"

    def purr(self) -> str:
        """
        Уникальный метод для кошек - мурлыканье.

        :return: Строка с описанием мурлыканья
        """
        return "Мурлычет от удовольствия"

    def __repr__(self) -> str:
        """Перегрузка repr с добавлением специфичных атрибутов."""
        return (f"{self.__class__.__name__}(name='{self.name}', age={self.age}, "
                f"habitat='{self.habitat}', breed='{self.breed}', "
                f"is_vaccinated={self.is_vaccinated})")


if __name__ == "__main__":
    # Пример использования
    animal = Animal("Неизвестное животное", 3, "лес")
    cat = Cat("Барсик", 2, "дом", "британец", True)

    print(animal)
    print(cat)

    print(animal.make_sound())  # Базовый метод
    print(cat.make_sound())  # Перегруженный метод
    print(cat.purr())  # Уникальный метод кошки

    try:
        animal.name = "Новое имя"  # Должно вызвать AttributeError
    except AttributeError as e:
        print(f"Ошибка: {e}")