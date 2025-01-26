from db.config import cursor
from utils.formatted_print import formatted_print


def airports_in_city():
    location = ""

    while location == "":
        location = input("Enter the name of the city: ")

    try:
        cursor.execute("SELECT * FROM Airport WHERE location = ?", (location,))
        descriptions = [x[0] for x in cursor.description]
        result = cursor.fetchall()
        formatted_print(descriptions, result)

    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
