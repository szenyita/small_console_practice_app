import sqlite3

class DatabaseManager:
    def __init__(self, db_path: str):
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Failed to connect to the database: {e}")
            raise

    def execute(self, query: str, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
        except sqlite3.Error as e:
            print(f"Query execution failed: {e}")
            raise

    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Fetch failed: {e}")
            raise

    def commit(self):
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Commit failed: {e}")
            raise

    def close(self):
        self.connection.close()

    @property
    def description(self):
        try:
            return self.cursor.description
        except sqlite3.Error as e:
            print(f"Failed to fetch description: {e}")
            raise
