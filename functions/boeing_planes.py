from db.config import cursor

def boeing_planes():
    query = "SELECT * FROM Plane"
    result = cursor.execute(query)

    for row in result:
        print(row)