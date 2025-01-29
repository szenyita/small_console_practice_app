class DatabaseManager:

    def __init__(self, db_path, sqlite3):
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Failed to connect to the database: {e}")
            raise

    def execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

        except Exception as e:
            print(f"Exception: {e}")

    def fetchall(self):
        try:
            return self.cursor.fetchall()

        except Exception as e:
            print(f"Exception: {e}")

    def commit(self):
        try:
            self.connection.commit()

        except Exception as e:
            print(f"Exception: {e}")

    def close(self):
        try:
            self.connection.close()

        except Exception as e:
            print(f"Exception: {e}")

    @property
    def description(self):
        try:
            return self.cursor.description

        except Exception as e:
            print(f"Exception: {e}")
