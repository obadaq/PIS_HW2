class Date:
    
    def __init__(self, day, month, year):

        self.months31 = [1, 3, 5, 7, 8, 10, 12]
        self.months30 = [4, 6, 9, 11]
        self.day = day
        self.month = month
        self.year = year

    def leap(self):
        if ((self.year % 400 == 0) or
                (self.year % 100 != 0) and
                (self.year % 4 == 0)):
            leap = True
        else:
            leap = False
            return leap

    def valid(self):
        if (1 <= self.month <= 12 and
            1 <= self.day <= 31 and (self.month in self.months31) or
            1 <= self.day <= 30 and (self.month in self.months30) or
                self.leap() and 1 <= self.day <= 29 or
                (not self.leap()) and 1 <= self.day <= 28):

            valid = True
        else:
            valid = False
            print('The Date you Entered is not VALID')
        return valid

    def order(self):
        order = 0
        if self.valid():
            for month in range(1, self.month):
                if month in self.months31:
                    order += 31
                elif month in self.months30:
                    order += 30
                elif self.leap:
                    order += 29
                else:
                    order += 28
            order += self.day
        return order

    def __add__(self, other):
        self.day = self.day + other
        return print(self)

    def __str__(self):
        return str(self.day) + '\\' + str(self.month) + '\\' + str(self. year)

    def __sub__(self, other):
        year_count = 0
        for year in range(self.year, other.year+1):
            if year.leap():
                year_count += 366
            else:
                year_count += 365

        return abs(self.order() - other.order()) + year_count



d1 = Date(10, 5, 2024)
d2 = Date(11, 5, 2023)

print(d1-d2)