class Date:
    def __init__(self, day: int, month: int, year: int):
        """
        Создание класса Date и проверка на передачу целочисленных значений
        :param day: день
        :param month: месяц
        :param year: год
        """
        self.day = day
        self.month = month
        self.year = year

        if not isinstance(day or month or year, int):
            raise TypeError

    def __repr__(self):
        return f"Результат работы метода __repr__: {self.day}/{self.month}/{self.year}"

    def __str__(self):
        return f"Результат работы метода __str__: {self.day}/{self.month}/{self.year}"


result_1 = Date(2, '45', 78)


print(result_1)

# TODO class Date
