from db.config import cursor, connection
from utils.is_date import is_date


def add_plane():
    print("Enter the following attributes:")

    plane_id = ""

    while len(plane_id) > 4 or len(plane_id) == 0:
        plane_id = input("Id (1-4 characters long): ")

    name = input("Name: ")
    plane_make = input("Make: ")

    date_of_creation = input("Date of creation (YYYY-MM-DD): ")

    while not is_date(date_of_creation):
        date_of_creation = input("Format is not in YYYY-MM-DD. Enter again: ")

    try:
        cursor.execute("SELECT plane_id FROM Plane")
        plane_ids = {x[0] for x in cursor.fetchall()}

        if plane_id in plane_ids:
            cursor.execute(
                """
                UPDATE Plane
                SET name = ?,
                plane_make = ?,
                date_of_creation = ?
                WHERE plane_id = ?
                """
                , (name, plane_make, date_of_creation, plane_id)
            )
            print("Plane updated successfully")

        else:
            cursor.execute("INSERT INTO Plane VALUES (?, ?, ?, ?)", (plane_id, name, plane_make, date_of_creation))
            print("Plane added successfully")


    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
