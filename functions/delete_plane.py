from db.config import cursor

def delete_plane():
    search = input("Enter the filter you would like to apply or skip with Enter: ")

    search = f"%{search}%"
    try:
        result = cursor.execute(
            """
            SELECT * FROM Plane
            WHERE
            plane_id LIKE ? OR
            name LIKE ? OR
            plane_make LIKE ? OR
            date_of_creation LIKE ?
            """, (search, search, search, search)
        )
        for row in result:
            print(row)

    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")

    plane_ids = cursor.execute(
        """
        SELECT plane_id FROM Plane
        WHERE
        plane_id LIKE ? OR
        name LIKE ? OR
        plane_make LIKE ? OR
        date_of_creation LIKE ?
        """, (search, search, search, search)
    )

    plane_id = input("Enter the Id of the plane you would like to delete: ")
    plane_ids = {x[0] for x in plane_ids}

    while plane_id not in plane_ids:
        plane_id = input("Id not found in filtered list of ids. Enter the correct Id: ")

    try:
        cursor.execute("DELETE FROM Plane WHERE plane_id = ?", (plane_id,))
    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")