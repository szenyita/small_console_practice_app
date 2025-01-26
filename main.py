from db.config import connection
from utils.messages import welcome, prompt
from functions.add_plane import add_plane
from functions.airports_in_city import airports_in_city
from functions.boeing_planes import boeing_planes
from functions.change_boeing_plane_name import change_plane_name
from functions.cities_with_boeing_in_dates import cities_with_boeing_in_dates
from functions.delete_plane import delete_plane

print(welcome)
while True:
    choice = input(prompt)

    match choice:
        case "1":
            boeing_planes()
        case "2":
            add_plane()
        case "3":
            change_plane_name()
        case "4":
            airports_in_city()
        case "5":
            delete_plane()
        case "6":
            cities_with_boeing_in_dates()
        case "7":
            connection.close()
            break
        case _:
            print("Invalid option")

    connection.commit()