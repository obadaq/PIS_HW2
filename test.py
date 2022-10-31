class Date:
    
    def __init__(self, day, month, year):
        self.months31 = [1, 3, 5, 7, 8, 10, 12]
        self.months30 = [4, 6, 9, 11]
        self.day = day
        self.month = month
        self.year = year
        if self.valid():
            print('This Date is Valid')
        else:
            print('This Date is NOT VALID')


    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def get_month(self):
        return self.month

    def set_month(self, month):
        self.month = month

    def get_year(self):
        return self.year

    def set_year(self, year):
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
                ((1 <= self.day <= 31 and (self.month in self.months31)) or
                 (1 <= self.day <= 30 and (self.month in self.months30)) or
                 (self.leap() and 1 <= self.day <= 29) or
                 (not self.leap()) and 1 <= self.day <= 28)):

            valid = True
        else:
            valid = False
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
        day = self.day + other
        month = self.month
        year = self.year
        new_date= Date(day,month,year)
        
        while not new_date.valid():
            if new_date.month in self.months31 and new_date.day > 31 :
                new_date.month += 1
                new_date.day -= 31

            elif new_date.month in self.months30 and new_date.day > 30:
                new_date.month += 1
                new_date.day -= 30

            elif new_date.leap() and new_date.month == 2 and new_date.day > 29:
                new_date.month += 1
                new_date.day -= 29

            elif not new_date.leap() and new_date.month == 2 and new_date.day > 28:
                new_date.month += 1
                new_date.day -= 28

            if new_date.month > 12:
                new_date.year += 1
                new_date.month = 1
        
        return new_date

    def __str__(self):
        return str(self.day) + '\\' + str(self.month) + '\\' + str(self. year)

    def __sub__(self, other):
        year_count = 0
        
        if self.year < other.year:
            rang = range(self.year, other.year)
        elif self.year > other.year:
            rang = range(other.year, self.year)

        for year in rang:
            if self.year == other.year:
                continue
            if ((year % 400 == 0) or
                (year % 100 != 0) and
                    (year % 4 == 0)):
                year_count += 366
            else:
                year_count += 365

        return abs(self.order() - other.order()) + year_count

    def __lt__(self, other):
        return self.order() < other

    def __gt__(self, other):
        return self.order() > other

    def __le__(self, other):
        return self.order() <= other

    def __ge__(self, other):
        return self.order() >= other

    def __eq__(self, other):
        return self.order() == other

    def __ne__(self, other):
        return self.order() != other