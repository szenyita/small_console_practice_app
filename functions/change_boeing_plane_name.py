from db.config import cursor

def change_plane_name():
    try:
        cursor.execute("SELECT * FROM Plane WHERE plane_make = 'Boieng'")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")

    choice = ""
    while choice not in {"Y", "N"}:
        choice = input("Would you like to change these names to \"Boeing\"? (Y/N):").upper()

    if choice == "Y":
        try:
            cursor.execute("UPDATE Plane SET plane_make = 'Boeing' WHERE plane_make = 'Boieng'")
        except Exception as e:
            print("Query failed")
            print(f"Exception {e}")
    else:
        return