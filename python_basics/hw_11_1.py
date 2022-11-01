class Date:
    def __init__(self, date):
        self.date = date
        self.day = None
        self.month = None
        self.year = None

    @classmethod
    def date_int(cls, self):
        day, month, year = str(self.date).split('-')
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        return self.day, self.month, self.year

    @staticmethod
    def valid_date(validation):
        day, month, year = validation
        try:
            assert 1 < day < 31, 'Incorrect day number, please use 1 to 31 numbers'
            assert 1 < month < 12, 'Incorrect month number, please use 1 to 12 numbers'
            assert len(str(year)) == 4, 'Incorrect year length, please use **** format'
        except AssertionError as error:
            raise error


expl = Date('24-04-2012')
Date.valid_date(Date.date_int(expl))
print(Date.date_int(expl))
print(expl.day)
print(expl.month)
print(expl.year)
