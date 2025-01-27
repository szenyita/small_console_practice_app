from db.config import cursor, connection


def create_views():
    cursor.execute(
        """
        CREATE VIEW IF NOT EXISTS Boeing AS
        SELECT * FROM Plane
        WHERE plane_make = 'Boeing'
        """
    )

    connection.commit()
