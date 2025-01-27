from db.config import cursor
from utils.formatted_print import formatted_print
from utils.is_date import is_date
from utils.get_descriptions import get_descriptions
from utils.to_csv_decorator import to_csv_decorator


@to_csv_decorator
def cities_with_boeing_in_dates():
    time_of_arrival = input("Time of arrival (YYYY-MM-DD): ")

    while not is_date(time_of_arrival):
        time_of_arrival = input("Format is not in YYYY-MM-DD. Enter again: ")

    time_of_departure = input("Time of departure (YYYY-MM-DD): ")

    while not is_date(time_of_departure):
        time_of_departure = input("Format is not in YYYY-MM-DD. Enter again: ")

    try:
        cursor.execute(
            """
            SELECT a.name FROM Airport a
            JOIN Schedule s ON a.airport_id = s.aiport_id
            JOIN Boeing b ON s.plane_id = b.plane_id
            WHERE time_of_arrival <= ?
            AND time_of_departure >= ?
            GROUP BY a.name
            """, (time_of_departure, time_of_arrival)
        )

        descriptions = get_descriptions(cursor.description)
        result = cursor.fetchall()
        has_records = formatted_print(descriptions, result)
        return descriptions, result, has_records

    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
