from db.config import cursor
from utils.formatted_print import formatted_print


def boeing_planes():
    try:
        cursor.execute("SELECT * FROM Plane WHERE plane_make = 'Boeing'")
        descriptions = [x[0] for x in cursor.description]
        result = cursor.fetchall()
        formatted_print(descriptions, result)
    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
