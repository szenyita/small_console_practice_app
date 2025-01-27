from db.config import cursor
from utils.formatted_print import formatted_print
from utils.get_descriptions import get_descriptions
from utils.to_csv_decorator import to_csv_decorator


@to_csv_decorator
def airports_in_city():
    location = ""

    while location == "":
        location = input("Enter the name of the city: ").lower()

    try:
        cursor.execute("SELECT * FROM Airport WHERE LOWER(location) = ?", (location,))
        descriptions = get_descriptions(cursor.description)
        result = cursor.fetchall()
        has_records = formatted_print(descriptions, result)

        return descriptions, result, has_records

    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
