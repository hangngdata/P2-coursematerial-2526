from datetime import date, timedelta

class Calendar:
    def __init__(self):
        self.today = date.today()

class CalendarStub:
    def __init__(self, today):
        self.today = today
    @property
    def today(self):
        return self.__today
    
    @today.setter
    def today(self, new_date):
        self.__today = new_date

calendar = CalendarStub(date(2000, 1, 1))

calendar.today = date(2001, 1, 1)
print(calendar.today)