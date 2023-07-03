"""Check a year is leap year or not"""


def check_leap_year(year: str) -> bool:
    year_int = int(year)
    if year_int % 4 == 0:
        if year_int % 100 == 0:
            if year_int % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    year = '123452'
    print(check_leap_year(year))