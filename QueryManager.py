from DatabaseManager import DatabaseManager
from Utility import Utility


class QueryManager:
    def __init__(self, db_manager: DatabaseManager, utility: Utility):
        self.db_manager = db_manager
        self.utility = utility
        self.create_indexes()
        self.create_views()

    def add_plane(self):
        print("Enter the following attributes:")

        plane_id = ""

        while len(plane_id) > 4 or len(plane_id) == 0:
            plane_id = input("Id (1-4 characters long): ")

        name = input("Name: ")
        plane_make = input("Make: ")

        date_of_creation = input("Date of creation (YYYY-MM-DD): ")

        while not self.utility.is_date(date_of_creation):
            date_of_creation = input("Format is not in YYYY-MM-DD. Enter again: ")

        self.db_manager.execute("SELECT plane_id FROM Plane")
        plane_ids = {x[0] for x in self.db_manager.fetchall()}

        if plane_id in plane_ids:
            self.db_manager.execute(
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
            self.db_manager.execute("INSERT INTO Plane VALUES (?, ?, ?, ?)", (plane_id, name, plane_make, date_of_creation))
            print("Plane added successfully")

    @Utility.to_csv_decorator
    def airports_in_city(self):
        location = ""

        while location == "":
            location = input("Enter the name of the city: ").lower()

        try:
            self.db_manager.execute("SELECT * FROM Airport WHERE LOWER(location) = ?", (location,))
            descriptions = self.utility.get_descriptions(self.db_manager.description)
            result = self.db_manager.fetchall()
            has_records = self.utility.formatted_print(descriptions, result)

            return descriptions, result, has_records

        except Exception as e:
            print("Query failed")
            print(f"Exception {e}")

    @Utility.to_csv_decorator
    def boeing_planes(self):
        try:
            self.db_manager.execute("SELECT * FROM Boeing")
            descriptions = self.utility.get_descriptions(self.db_manager.description)
            result = self.db_manager.fetchall()
            has_records = self.utility.formatted_print(descriptions, result)

            return descriptions, result, has_records

        except Exception as e:
            print("Query failed")
            print(f"Exception {e}")

    def change_plane_name(self):
        try:
            self.db_manager.execute("SELECT * FROM Plane WHERE plane_make = 'Boieng'")
            descriptions = self.utility.get_descriptions( self.db_manager.description)
            result = self.db_manager.fetchall()

            if not self.utility.formatted_print(descriptions, result):
                return

        except Exception as e:
            print("Query failed")
            print(f"Exception {e}")

        choice = ""

        while choice not in {"Y", "N"}:
            choice = input("Would you like to change these names to \"Boeing\"? (Y/N): ").upper()

        if choice == "Y":
            try:
                self.db_manager.execute("UPDATE Plane SET plane_make = 'Boeing' WHERE plane_make = 'Boieng'")
                print("Plane name changed successfully")

            except Exception as e:
                print("Query failed")
                print(f"Exception {e}")

    @Utility.to_csv_decorator
    def cities_with_boeing_in_dates(self):
        time_of_arrival = input("Time of arrival (YYYY-MM-DD): ")

        while not self.utility.is_date(time_of_arrival):
            time_of_arrival = input("Format is not in YYYY-MM-DD. Enter again: ")

        time_of_departure = input("Time of departure (YYYY-MM-DD): ")

        while not self.utility.is_date(time_of_departure):
            time_of_departure = input("Format is not in YYYY-MM-DD. Enter again: ")

        try:
            # Applying the filters in the query is more efficient than doing so in the Python code.
            # If we were to select all the data from our database and then looped through the returned values
            # either with a loop or by a built-in function like filter() (which uses looping under the hood)
            # we would add an algorithm which costs O(n) time for no reason.

            self.db_manager.execute(
                """
                SELECT DISTINCT a.name FROM Airport a
                JOIN Schedule s ON a.airport_id = s.aiport_id
                JOIN Boeing b ON s.plane_id = b.plane_id
                WHERE time_of_arrival <= ?
                AND time_of_departure >= ?
                """, (time_of_departure, time_of_arrival)
            )

            descriptions = self.utility.get_descriptions(self.db_manager.description)
            result = self.db_manager.fetchall()
            has_records = self.utility.formatted_print(descriptions, result)

            return descriptions, result, has_records

        except Exception as e:
            print("Query failed")
            print(f"Exception {e}")

    def delete_plane(self):
        search = input("Enter the filter you would like to apply or skip with Enter: ")
        search = f"%{search}%"
        result = []

        try:
            self.db_manager.execute(
                """
                SELECT * FROM Plane
                WHERE plane_id LIKE ?
                OR name LIKE ?
                OR plane_make LIKE ?
                OR date_of_creation LIKE ?
                """, (search, search, search, search)
            )
            descriptions = self.utility.get_descriptions(self.db_manager.description)
            result = self.db_manager.fetchall()
            self.utility.formatted_print(descriptions, result)

        except Exception as e:
            print("Query failed")
            print(f"Exception {e}")

        plane_id = input("Enter the Id of the plane you would like to delete: ")
        plane_ids = {row[0] for row in result}

        while plane_id not in plane_ids:
            plane_id = input("Id not found in filtered list of ids. Enter the correct Id: ")

        try:
            self.db_manager.execute("DELETE FROM Plane WHERE plane_id = ?", (plane_id,))
            print("Plane deleted successfully")

        except Exception as e:
            print("Query failed")
            print(f"Exception {e}")

    def create_indexes(self):
        self.db_manager.execute(
            """
            CREATE INDEX IF NOT EXISTS
            Plane_make_idx ON Plane(plane_make)
            """
        )

        self.db_manager.commit()

    def create_views(self):
        self.db_manager.execute(
            """
            CREATE VIEW IF NOT EXISTS Boeing AS
            SELECT * FROM Plane
            WHERE plane_make = 'Boeing'
            """
        )

        self.db_manager.commit()
