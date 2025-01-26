from db.config import cursor
from utils.formatted_print import formatted_print


def change_plane_name():
    try:
        cursor.execute("SELECT * FROM Plane WHERE plane_make = 'Boieng'")
        descriptions = [x[0] for x in cursor.description]
        result = cursor.fetchall()
        if not formatted_print(descriptions, result):
            return

    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")

    choice = ""

    while choice not in {"Y", "N"}:
        choice = input("Would you like to change these names to \"Boeing\"? (Y/N):").upper()

    if choice == "Y":
        try:
            cursor.execute("UPDATE Plane SET plane_make = 'Boeing' WHERE plane_make = 'Boieng'")
            print("Plane name changed successfully")

        except Exception as e:
            print("Query failed")
            print(f"Exception {e}")
