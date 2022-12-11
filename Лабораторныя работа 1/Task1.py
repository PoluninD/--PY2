import doctest
from typing import Union

class Volcano:
    def __init__(self, name:str , hight_over_sea: Union[int,float] ,status:str, last_eruption_year: int):
        """ Создание и подготовка объекта "Вулкан"
          :param name: Название вулкана
          :param hight_over_sea: Высота вулкана над уровнем моря
          :param status: Стату вулкана активный он или нактивный
          :param last_eruption_year: Год последнего извержения вулкана

          Пример :
          >>> volcano1 = Volcano("Везувий",1234, "Не активный", 1986) # инициализация объекта класса
        """
        if not isinstance(name , str):
            raise TypeError ("Название Вулкана должно быть типа str")
        self.name = name
        if not isinstance(hight_over_sea, (int,float)):
            raise TypeError ("Значение высоты над уровнем моря должно иметь тип int или float")
        self.hight_over_sea = hight_over_sea

        if not isinstance(status , str):
            raise TypeError ("Статус вулкана должно быть типа str")
        self.status = status

        if not isinstance(last_eruption_year, int ):
            raise TypeError ("Год последгего извержения должен быть int")
        self.last_eruption_year = last_eruption_year

    def volcano_errupt(self , current_year:int):
        """
        Метод меняющий дату посленего извержения
        :param current_year: Текущий год т.е. год когд мы наблюдаем извержение
        :return: Год последнего извержения

        >>> volcano1 = Volcano("Везувий",1234, "Не активный", 1986)
        >>> volcano1.volcano_errupt(2011)
        """

        ...
    def is_volcano_active(self) ->bool :
        """
        Функция определяющая является ли вулкан актаным
        :return: Вулкан является Активынм
        Пример:
        >>> volcano1 = Volcano("Везувий",1234, "Не активный", 1986)
        >>> volcano1.is_volcano_active()
        """
        ...
    def volc_growth(self,val:Union[int, float]):
        """Метод демонстрирующий изменение высоты вулкана в
        результате геологический процессов
        :param val: Демонстрирует значение на которое увеличилась или уменьшилась высота вулкана
        :raise TypeError: Если тип данных не int или float вызываем ошибку
        :return: Изменеённое значение высоты вулкана
        Пример:
        >>> volcano1 = Volcano("Везувий",1234, "Не активный", 1986)
        >>> volcano1.volc_growth(-15)
        """
        ...

class Locker:
    def __init__(self,capacity: int , clothes_now: int, color:str):
        """
        Подготавливаем класс к работе с ним
        :param capacity: Максимальное кол-во вещей которые влезают в шкаф
        :param clothes_now: Кол-во вещей которые сейчас находятся в шкафу
        :param color: Цвет шкафа
        Пример:
        >>> locker_t = Locker(14,5, "Brown")
        """
        if not isinstance(capacity,int):
            raise  TypeError("вместимость должна быть целым числом")
        if capacity <=0:
            raise ValueError ("Вместимость должна быть положительным число > 0 ")
        self.capacity = capacity

        if not isinstance(clothes_now,int):
            raise  TypeError("Число вещей в шкафу должно быть int")
        if clothes_now < 0:
            raise ValueError ("Число вещей не может быть отрицательным")
        self.clothes_now = clothes_now

        if not isinstance(color,str):
            raise  TypeError("Цвет должен быть типом str ")
        self.color = color

    def drop_cloth(self, num) -> None:
        """
        Метод позволяющий заеинуть определённое число в шкаф
        :param num: Число вещей которые вы закинули в шкаф
        :raise ValueError: Число вещей которые вы хотите закинуть  должно быть >=0
        :return: число вещей в шкафу
        Пример:
        >>> locker_t = Locker(14,5, "Brown")
        >>> locker_t.drop_cloth(13)
        """
        ...
    def paint_it(self, new_col:str) -> None:
        """
        Метод меняющий цвет нашего шкафа

        :param new_col:
        :raise TypeError: Если введённые данные не являются str
        :return: Шкаф перекрашенный в новый цвет
        Пример:
        >>> locker_t = Locker(14,5, "Brown")
        >>> locker_t.paint_it("green")

        """
        ...

class Fish:
    def __init__(self, name:str , age: int, status:str):
        """
        Подготавливаем к работе класс "Рыба"
        :param name: Имя рыбы
        :param age: Возраст рыбы
        :param status: Голодная рыба или нет
        Пример:
        >>> fish1 = Fish("Boy" , 4 , "Голодная")
        """
        if not isinstance(name , str):
            raise TypeError("Имя должно быть типом str")
        self.name = name

        if not isinstance(age, int ):
            raise TypeError("Возраст должен быть int типом")
        if age < 0:
            raise ValueError("Возраст не может быть меньше нуля")
        self.age = age

        if not isinstance(status, str):
            raise TypeError("Состояние должно быиь типом str")
        self.status = status

    def feed_fish(self) -> None:
        """
            Метод меняющий состояние рыбы на "Сытый"
        :return: Сытая рыба
        Пример:
        >>> fish1 = Fish("Boy" , 4 , "Голодная")
        >>> fish1.feed_fish()
        """
        ...
    def years_passed(self,years:int ) -> None:
        """
        Метод демонстрирующий взросление рыбки
        :param years: Число лет которое полжила рыба
        :return: Выросшую рыбу
        Пример:
        >>> fish1 = Fish("Boy" , 4 , "Голодная")
        >>> fish1.years_passed(5)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()

