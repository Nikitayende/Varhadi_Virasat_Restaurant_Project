import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Add new columns if they don't already exist
columns = [
    ("area", "TEXT"),
    ("position", "TEXT"),
    ("status", "TEXT DEFAULT 'Available'")
]

for name, datatype in columns:
    try:
        cursor.execute(f"ALTER TABLE restaurant_tables ADD COLUMN {name} {datatype}")
        print(f"{name} added")
    except Exception:
        print(f"{name} already exists")

conn.commit()
conn.close()

print("Database Updated")