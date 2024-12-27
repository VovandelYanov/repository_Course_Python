# TODO: описать базовый класс

class Laptop:  # базовый класс для всех ноутбуков

    def __init__(self, brand: str, model: str, ram: int, storage: int):
        """
        :param brand: Бренд ноутбука.
        :param model: Модель ноутбука.
        :param ram: Объем оперативной памяти.
        :param storage: Объем накопителя.
        """
        self._brand = brand  # непубличный атрибут для бренда
        self._model = model  # непубличный атрибут для модели
        self._ram = ram  # непубличный атрибут для оперативной памяти
        self._storage = storage  # непубличный атрибут для накопителя

    def specifications(self) -> str:  # метод, который должен быть переопределен в дочерних классах
        """
        :return: спецификации ноутбука.
        """
        raise NotImplementedError("метод specifications() должен быть переопределен в дочернем классе.")

    def __str__(self) -> str:  # возвращает строковое представление ноутбука
        """
        :return: Строка с информацией о ноутбуке.
        """
        return f"{self._brand} {self._model}, RAM: {self._ram}GB, Storage: {self._storage}GB"

    def __repr__(self) -> str:  # возвращает официальное строковое представление ноутбука
        """
        :return: Официальная строка с информацией о ноутбуке.
        """
        return f"Laptop(brand={self._brand}, model={self._model}, ram={self._ram}, storage={self._storage})"


# TODO: описать дочерний класс

class GamingLaptop(Laptop):  # дочерний класс игровых ноутбуков

    def __init__(self, brand: str, model: str, ram: int, storage: int, gpu: str):
        """
        :param brand: Бренд игрового ноутбука.
        :param model: Модель игрового ноутбука.
        :param ram: Объем оперативной памяти.
        :param storage: Объем накопителя.
        :param gpu: Модель видеокарты.
        """
        super().__init__(brand, model, ram, storage)  # вызов конструктора базового класса
        self._gpu = gpu  # непубличный атрибут для видеокарты

    def specifications(self) -> str:
        """
        :return: Строка с информацией о характеристиках.
        """
        return f"{self} - GPU: {self._gpu}"

    def __str__(self) -> str:  # возвращает строковое представление игрового ноутбука
        """
        :return: Строка с информацией о игровом ноутбуке.
        """
        return super().__str__() + f", GPU: {self._gpu}"

    def __repr__(self) -> str:  # возвращает строковое представление игрового ноутбука
        """
        :return: Официальная строка с информацией о игровом ноутбуке.
        """
        return f'GamingLaptop(brand={self._brand}, model={self._model}, ram={self._ram}, storage={self._storage}, gpu={self._gpu})'


class OfficeLaptop(Laptop):  # дочерний класс офисных ноутбуков

    def __init__(self, brand: str, model: str, ram: int, storage: int, battery_life: int):
        """
        :param brand: Бренд офисного ноутбука.
        :param model: Модель офисного ноутбука.
        :param ram: Объем оперативной памяти.
        :param storage: Объем накопителя.
        :param battery_life: Время работы от батареи.
        """
        super().__init__(brand, model, ram, storage)  # вызов конструктора базового класса
        self._battery_life = battery_life  # непубличный атрибут для времени работы от батареи

    def specifications(self) -> str:
        """
        :return: Строка с информацией о характеристиках.
        """
        return f"{self} - Battery Life: {self._battery_life} hours"

    def __str__(self) -> str:   # возвращает строковое представление офисного ноутбука
        """
        :return: Строка с информацией о офисном ноутбуке.
        """
        return super().__str__() + f", Battery Life: {self._battery_life} hours"

    def __repr__(self) -> str:      # возвращает официальное строковое представление офисного ноутбука
        """
        :return: Официальная строка с информацией о офисном ноутбуке.
        """
        return f"OfficeLaptop(brand={self._brand}, model={self._model}, ram={self._ram}, storage={self._storage}, " \
               f"battery_life={self._battery_life})"
