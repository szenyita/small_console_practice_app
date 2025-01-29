from DatabaseManager import DatabaseManager
from Utility import Utility
from QueryManager import QueryManager
from App import App

def main():
    db_path = "db/airplanes.db3"

    db_manager = DatabaseManager(db_path)
    utility = Utility()
    query_manager = QueryManager(db_manager, utility)
    app = App(db_manager, query_manager, utility)

    app.run()

    db_manager.close()

if __name__ == "__main__":
    main()
