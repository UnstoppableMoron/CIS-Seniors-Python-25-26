class Date:
    """Represents a year, month, and day"""
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0

def make_date(year, month, day):
    d = Date()
    d.year = year
    d.month = month
    d.day = day
    return d

def print_date(date):
    print(f"{date.year}-{date.month}-{date.day}")

def date_to_tuple(date):
    return (date.year, date.month, date.day)

def is_after(d1, d2):
    return date_to_tuple(d1) > date_to_tuple(d2)

d1 = make_date(1933, 6, 22)
d2 = make_date(1933, 9, 17)

print_date(d1)
print_date(d2)

print(is_after(d2, d1))