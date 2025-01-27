from db.config import cursor
from utils.formatted_print import formatted_print
from utils.get_descriptions import get_descriptions


def delete_plane():
    search = input("Enter the filter you would like to apply or skip with Enter: ")
    search = f"%{search}%"
    result = []

    try:
        cursor.execute(
            """
            SELECT * FROM Plane
            WHERE plane_id LIKE ?
            OR name LIKE ?
            OR plane_make LIKE ?
            OR date_of_creation LIKE ?
            """, (search, search, search, search)
        )
        descriptions = get_descriptions(cursor.description)
        result = cursor.fetchall()
        formatted_print(descriptions, result)

    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")

    plane_id = input("Enter the Id of the plane you would like to delete: ")
    plane_ids = {row[0] for row in result}

    while plane_id not in plane_ids:
        plane_id = input("Id not found in filtered list of ids. Enter the correct Id: ")

    try:
        cursor.execute("DELETE FROM Plane WHERE plane_id = ?", (plane_id,))
        print("Plane deleted successfully")

    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
