import sqlite3

conn = sqlite3.connect("data/database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    date_applied TEXT NOT NULL,
    status TEXT NOT NULL,
    notes TEXT
)
""")

conn.commit()

conn.close()

print("Database and table created successfully!")