class App:

    def __init__(self, db_manager, query_manager, utility):
        self.db_manager = db_manager
        self.query_manager = query_manager
        self.utility = utility

    def run(self):
        print(self.utility.welcome)

        self.query_manager.create_indexes()
        self.query_manager.create_views()

        while True:
            choice = input(self.utility.prompt)

            match choice:
                case "1":
                    self.query_manager.boeing_planes()
                case "2":
                    self.query_manager.add_plane()
                case "3":
                    self.query_manager.change_plane_name()
                case "4":
                    self.query_manager.airports_in_city()
                case "5":
                    self.query_manager.delete_plane()
                case "6":
                    self.query_manager.cities_with_boeing_in_dates()
                case "7":
                    self.db_manager.close()
                    print(self.utility.goodbye)
                    break
                case _:
                    print("Invalid option")

            self.db_manager.commit()
