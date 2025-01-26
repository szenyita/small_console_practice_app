from db.config import cursor

def boeing_planes():
    try:
        result = cursor.execute("SELECT * FROM Plane WHERE plane_make = 'Boeing'")
        print([x[0] for x in cursor.description])
        for row in result:
            print(row)
    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
