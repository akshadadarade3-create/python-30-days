"""Add a @staticmethod that validates the date string format. """
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def validate_date(date_string):
        try:
            day, month, year = date_string.split("-")

            if len(day) != 2 or len(month) != 2 or len(year) != 4:
                return False
            day = int(day)
            month = int(month)
            year = int(year)
            if year < 1 or month < 1 or month > 12:
                return False
            import calendar
            return 1 <= day <= calendar.monthrange(year, month)[1]
        except ValueError:
            return False

    @classmethod
    def from_string(cls, date_string):
        if not cls.validate_date(date_string):
            raise ValueError("Invalid date!")
        day, month, year = date_string.split("-")
        return cls(int(day), int(month), int(year))
    def show_date(self):
        print(f"{self.day:02d}-{self.month:02d}-{self.year:04d}")

d1 = Date.from_string("03-01-2006")
d1.show_date()
print(Date.validate_date("31-02-2026"))
