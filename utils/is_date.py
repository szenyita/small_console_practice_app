from re import search

pattern = "\d{4}-\d{2}-\d{2}"

def is_date(date_of_creation):
    if len(date_of_creation) == 10 and search(pattern, date_of_creation):
        return True
    return False