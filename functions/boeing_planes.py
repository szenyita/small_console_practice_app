from db.config import cursor
from utils.formatted_print import formatted_print
from utils.to_csv_decorator import to_csv_decorator


@to_csv_decorator
def boeing_planes():
    try:
        cursor.execute("SELECT * FROM Plane WHERE plane_make = 'Boeing'")
        descriptions = [x[0] for x in cursor.description]
        result = cursor.fetchall()
        has_records = formatted_print(descriptions, result)
        return descriptions, result, has_records

    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
