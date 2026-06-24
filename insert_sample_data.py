import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO applications
(company, role, date_applied, status, notes)
VALUES
('IBM', 'ASE', '23-06-2026', 'Applied', 'Waiting')
""")

cursor.execute("""
INSERT INTO applications
(company, role, date_applied, status, notes)
VALUES
('Infosys', 'SE', '20-06-2026', 'Rejected', 'Not Selected')
""")

cursor.execute("""
INSERT INTO applications
(company, role, date_applied, status, notes)
VALUES
('TCS', 'Ninja', '25-06-2026', 'Applied', 'Preparing')
""")

cursor.execute(
    "SELECT id, company, role, date_applied, status FROM applications"
)

conn.commit()
conn.close()

print("Sample records inserted successfully!")