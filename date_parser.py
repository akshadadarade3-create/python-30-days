""" a @classmethod that builds an object from a string like 18-09-2026"""
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = date_string.split("-")
        return cls(int(day), int(month), int(year))
    def show_date(self):
        print("Date:", self.day, self.month, self.year)

d1 = Date.from_string("03-01-2006")
d1.show_date()
