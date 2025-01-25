import sqlite3

connection = sqlite3.connect("db/airplanes.db3")
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

print(cursor.fetchall())