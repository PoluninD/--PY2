import doctest

class Character:
    def __init__(self,name:str = None, health: int = 100 , atck: int = 5, armor: int = 1):
        """
        Создание и подготовка объекта Персонаж
        :param name: Имя персонажа
        :param health: Показатель здоровья
        :param atck: Значение атаки персонажа
        :param armor: Значение защиты персонажа
        Пример:
        >>> char1 = Character("Serega",150 , 30, 10 ) # инициализация объекта класса
        """
        if not isinstance(name,str):
            raise TypeError("Имя должно быть str")
        self.name = name

        if not isinstance(health,int):
            raise TypeError("Значение здоровья должно быть int типом")
        if health <= 0:
            raise ValueError("Значение здоровья должно быть больше нуля")
        self.health = health

        if not isinstance(atck,int):
            raise TypeError("Значение атаки должно быть int типом")
        if atck < 0:
            raise ValueError("Значение атаки должно быть не меньше нуля")
        self.atck = atck

        if not isinstance(armor,int):
            raise TypeError("Значение зашиты должно быть int типом")
        if armor < 0:
            raise ValueError("Значение защиты должно быть не меньше нуля")
        self.armor = armor

    def take_armor(self,val: int):
        """
        Метод увеличивающий значнение зашиты на величину val
        :param val: Значение на которое повышается показатель брони
        :return: Значение защиты увеличенное на val
        >>> char1 = Character("Peter",120 , 10, 10 )
        >>> char1.take_armor(7)
        """
        if not isinstance(val,int):
            raise TypeError("Значение зашиты должно быть int типом")
        if val < 0:
            raise ValueError("Значение защиты должно быть не меньше нуля")
        self.armor = self.armor+ val

    def take_weapon(self,num: int):
        """
        Метод увеличивающий значнение атаки на величину num
        :param val: Значение на которое повышается показатель атаки
        :return: Значение атаки увеличенное на val
        >>> char1 = Character("Peter",120,10,10)
        >>> char1.take_weapon(10)
        """
        if not isinstance(num,int):
            raise TypeError("Значение атаки должно быть int типом")
        if num < 0:
            raise ValueError("Значение атаки должно быть не меньше нуля")
        self.atck = self.atck + num



    def __str__(self):
        return f"Персонаж {self.name}.Показатель здоровья = {self.health}.С атакой = {self.atck}.И зашитой = {self.armor}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r},health = {self.health!r}, atck ={self.atck!r},armor = {self.armor!r})"

class MainCharacter(Character):
    def __init__(self,nickname:str = ' _ ', name : str = None, health: int = 200, atck: int = 15 ,  armor:int = 10,):
        """
        Создание и подготовка объекта Главный персонаж доченрнего по отношению к Character
        С изменёнными значениями атрибутов по умолчанию
        :param nickname: Кличка главнрого персонажа
        :param name: имя героя
        :param health: значение здоровья персонажа
        :param atck: значение атаки героя
        :param armor: показатенль брони
        Пример:
        >>> main1 = MainCharacter("Zore","Will",300,14,20)
        """
        super().__init__(name, health, atck, armor)
        self.nickname = nickname

    @property
    def nickname(self) -> str:
        return self._nickname
    @nickname.setter
    def nickname(self, nickname: str) -> None:
        if not isinstance(nickname,str):
            raise TypeError("nickname должен быть типа str")
        self._nickname = nickname
    """Проверка типов с помощью свойствс, с использованием защищённых данных 
    для "использования" их только в своствах"""

    def take_armor(self,val: int):
        """
        Метод увеличивающий показатель брони main char
        :param val: значение на которое увеличиваем защиту
        :return: Увеличенноне на значение val*2 значение брони
        >>> main1 = MainCharacter("Slasher","Tom",150,13,2)
        >>> main1.take_armor(4)
        """
        self.armor = self.armor + val * 2
    """Перегрузил метод так как значения брони получаемые Главным персонажем должны быть выше чем у остальных"""

    def __str__(self):
        return f"Персонаж {self.name}, кличка - {self.nickname}.Показатель здоровья = {self.health}.С атакой = {self.atck}.И зашитой = {self.armor}"
    """Перегрузил str т.к. появился новый важный для пользовтеля атрибут nickname"""

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r},nickname = {self.nickname!r},health = {self.health!r}, atck ={self.atck!r},armor = {self.armor!r})"
    """Перегрузил из-за наличия нового атрибута в классе"""
    ...

class Enemy(Character):

    def __init__(self,name:str = "base enemy" , behavior:str = "Neutral"):
        """
        Дочерний объект по отношению к Character наследующий атрибуты кроме name и все методы кроме repr
        name не наследуется так как name у каждого из персонаджей своё и этот атрибут
        постоянно меняется поэтому в классе char он не является privat
        :param name: Имя врага
        :param behavior: Поведение врага
        Пример:
        >>> enemy1 = Enemy("Abaray", "Agressive") # Остальные атрибуты Character по-умолчанию

        """
        super().__init__(name)
        self.behavior = behavior

    @property
    def behavior(self) -> str:
        return self._behavior
    @behavior.setter
    def behavior(self, behavior: str) -> None:
        if not isinstance(behavior, str):
            raise TypeError("behavior должен быть типа str")
        self._behavior = behavior
    """Проверка типа данных атрибута behavior, с использованием защищённых данных 
    для "использования" их только в своствах"""

    def taunt_enemy(self):
        """Метод меняющий поведение врага на агресивное
        :return: Агрессивное поведение
        >>> enemy1 = Enemy()
        >>> enemy1.taunt_enemy()
        """
        self.behavior = "Agressive"

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r},behavior = {self.behavior!r},health = {self.health!r}, atck ={self.atck!r},armor = {self.armor!r})"
    """Перегрузил метод т.к. появился новый атрибут behavior
       в то же время класс наследует и все атрибутоы и омтавшиеся методы
       базового класса """

    ...

if __name__ == "__main__":
    doctest.testmod()
    pass
