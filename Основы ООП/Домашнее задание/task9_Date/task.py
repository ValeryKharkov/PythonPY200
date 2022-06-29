class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

        if not isinstance(self.day, int):
            raise TypeError("Значения должны быть int")
        if not isinstance(self.month, int):
            raise TypeError("Значения должны быть int")
        if not isinstance(self.year, int):
            raise TypeError("Значения должны быть int")

    def __repr__(self):
        ...

    def __str__(self):
        self.is_two_digit_day()
        self.is_two_digit_month()
        return f"__str__: {self.day}/{self.month}/{self.year}"

    def is_two_digit_day(self):
        if len(str(self.day)) == 1:
            self.day = '0' + str(self.day)
            return str(self.day)

    def is_two_digit_month(self):
        if len(str(self.month)) == 1:
            self.month = '0' + str(self.month)
            return str(self.month)


date = Date(9, 10, 2012)
print(date)

#  class Date
