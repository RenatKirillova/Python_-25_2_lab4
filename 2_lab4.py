if __name__ == "__main__":
    # Write your solution here
    pass

class Book:
    """
    Базовый класс
    """
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание объекта книги

        :param title: название книги
        :param author: автор книги
        :param pages: колличество страниц
        """
        if not isinstance(title, str):
            raise TypeError ("title must be str")
        if title == "":
            raise ValueError("title cannot be empty")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("author must be str")
        if author == "":
            raise ValueError("author cannot be empty")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("pages must be int")
        if pages <= 0:
            raise ValueError("pages must be positive")
        self.pages = pages

def __str__(self):
    """
    Представление объекта для пользователя

    :return: основная информация о книге
    """
    return f"Книга: {self.title}, автор: {self.author}, страниц: {self.pages}"
def __repr__(self):
    """
    Техническое представление объекта

    :return: стррка отладки
    """
    return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"

def open_book(self):
    """
    Открыть книгу

    :return: сообщение об открытии книги
    """
    return f"Книга '{self.title}' Открыта"
def get_info(self):
    """
    получить информацию о книге

    :return: краткая информация о книге
    """
    return f"{self.title} - {self.author}"

def read(self, page: int):
    """
    Читать книгу с указанной страницы

    :param page: номер страницы
    :return: сообщение о чтении

    :raise TypeError: если page не целое число
    :raise ValueError: если номер страницы выходит за границы
    """
    if not isinstance(page, int):
        raise TypeError("page must be int")
    if page <= 0 or page > self.pages:
        raise f"Чтение книги '{self.title}' со страницы {page}"



class Ebook(Book):
    """
    очерний класс
    """
    def __init__(self, title: str, author: str, pages: int, file_size: float, file_format: str):
        """
        Cоздание объекта эдектронной книги
        :param title:
        :param author:
        :param pages:
        :param file_size:
        :param file_format:
        """
        super().__init__(title, author, pages)

        if not isinstance(file_size, (int, float)):
            raise TypeError("file_size must be number")
        if file_size <= 0:
            raise ValueError("file_size must be positive")
        self.file_size = file_size

        if not isinstance(file_format, str):
            raise TypeError("file_format must be str")
        if file_format == "":
            raise ValueError("file_format cannot be empty")
        self.file_format = file_format
        self.device_charge = 100

def __str__(self):
    """

    :return:
    """
    return f"Электронная книга: {self.title}, автор: {self.author}, формат: {self.file_format}"

def __repr__ (self):
    return (
        f"EBook(title={self.title!r}, author={self.author!r}, pages={self.pages!r}, "
        f"file_size={self.file_size!r}, file_format={self.file_format!r})"
    )
def read(self,page: int) -> str:
    """
    читать книгу с указанной стр.
    метод перегружен тк чтение засит еще и от уровня заряда устройства

    :param page: номер страницы
    :return: сообщение о чтении

    :raise TypeError: если page не целое число
    :raise ValueError: если номер страницы выходит за пределы допустимого
    """
    if not isinstance(page, int):
        raise TypeError("page must be int")
    if page <= 0 or page > self.pages:
        raise ValueError("incorrect page number")
    if self._device_charge <= 0:
        return "Устройство разряжено, чтение невозможно"
    return f"Чтение электронной книги '{self.title}' со страницы {page} в формате {self.file_format}"

    def download(self):
        return f"Книга '{self.title}' скачана в формате {self.file_format}"

    def charge_device(self, value: int):
        
        if not isinstance(value, int):
         raise TypeError("value must be int")
        if value < 0:
         raise ValueError("value cannot be negative")


        self._device_charge += value
        if self._device_charge > 100:
         self._device_charge = 100
         return f"Заряд устройства: {self._device_charge}%"