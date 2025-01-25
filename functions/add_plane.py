from db.config import cursor, connection
from re import search

def add_plane():
    cursor.execute("SELECT plane_id FROM Plane")
    plane_ids = {x[0] for x in cursor.fetchall()}

    print("Enter the following attributes:")

    plane_id = ""
    while len(plane_id) != 4 or plane_id in plane_ids:
        plane_id = input("Id (4 characters and unique): ")
        if len(plane_id) != 4:
            print("Id is not 4 characters long")
        if plane_id in plane_ids:
            print("Id is not unique")

    name = input("Name: ")
    plane_make = input("Make: ")

    pattern = "\d{4}-\d{2}-\d{2}"
    date_of_creation = ""
    while len(date_of_creation) != 10 or not search(pattern, date_of_creation):
        date_of_creation = input("Date of creation (YYYY-MM-DD): ")
        if len(date_of_creation) != 10:
            print("Date of creation is not 10 characters long")
        if not search(pattern, date_of_creation):
            print("Date of creation format is not (YYYY-MM-DD)")

    try:
        cursor.execute("INSERT INTO Plane VALUES (?, ?, ?, ?)", (plane_id, name, plane_make, date_of_creation))
        connection.commit()
    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
