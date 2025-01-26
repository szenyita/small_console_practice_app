from re import search


pattern = "\d{4}-\d{2}-\d{2}"

def is_date(date_of_creation):
    if len(date_of_creation) == 10 and search(pattern, date_of_creation):
        is_leap_year = False
        year = int(date_of_creation.split("-")[0])
        month = int(date_of_creation.split("-")[1])
        day = int(date_of_creation.split("-")[2])

        if year % 400 == 0:
            is_leap_year = True
        elif year % 100 == 0:
            is_leap_year = False
        elif year % 4 == 0:
            is_leap_year = True

        if month == 0 or month > 12 or day == 0 or day > 31:
            return False

        if is_leap_year and month == 2 and day > 29:
            return False

        elif not is_leap_year and month == 2 and day > 28:
            return False

        return True

    return False
