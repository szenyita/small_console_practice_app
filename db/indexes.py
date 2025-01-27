
from db.config import cursor, connection


def create_indexes():
    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS
        Plane_make_idx ON Plane(plane_make)
        """
    )

    connection.commit()
