def is_year_leap(year):
            if year < 1582:
                return False
    
            elif year % 4 != 0:
                return False
            elif year % 100 != 0:
                return True
            elif year % 400 != 0:
                return False
            else:
                return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    return month_days[month]

def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12:
        return None
    max_days = days_in_month(year, month)
    if day < 1 or day > max_days:
        return None
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    total_days += day
    
    return total_days

print(day_of_year(2000, 12, 31))
