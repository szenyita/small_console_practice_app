from Classes.DatabaseManager import DatabaseManager
from Classes.Utility import Utility
from Classes.QueryManager import QueryManager
from Classes.App import App
import sqlite3
from textwrap import dedent
from re import search
import csv

def main():
    db_path = "db/airplanes.db3"

    db_manager = DatabaseManager(db_path, sqlite3)
    utility = Utility(dedent, search, csv)
    query_manager = QueryManager(db_manager, utility)
    app = App(db_manager, query_manager, utility)

    app.run()

    db_manager.close()

if __name__ == "__main__":
    main()
