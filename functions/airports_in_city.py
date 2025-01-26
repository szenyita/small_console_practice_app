from db.config import cursor

def airports_in_city():
    location = ""
    while location == "":
        location = input("Enter the name of the city: ")

    try:
        result = cursor.execute("SELECT * FROM Airport WHERE location = ?", (location,))
        print([x[0] for x in cursor.description])
        for row in result:
            print(row)
    except Exception as e:
        print("Query failed")
        print(f"Exception {e}")
