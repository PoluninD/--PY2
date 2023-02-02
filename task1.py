class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):

        if not isinstance(name,str):
            raise TypeError("Название должно быть str")
        else:
            self._name = name

        if not isinstance(author ,str):
            raise TypeError("Автор должен  быть str")
        else:
            self._author = author
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self,name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Должно быть целочисленным")
        if pages < 0  :
            raise ValueError("Страниц не может быть меньше чем ноль")
        self._pages = pages

class AudioBook(Book):
    def __init__(self,name: str, author: str,duration: float):
        super().__init__(name , author )
        self.duration = duration
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration,float):
            raise TypeError("Должно быть числом с плавающей запятой")
        if duration < 0:
            raise ValueError("Продожительность не может быть меньше нуля")
        self._duration = duration




