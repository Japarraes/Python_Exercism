def leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 400):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leap_year(2000))