import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM applications")

conn.commit()
conn.close()

print("All records deleted.")