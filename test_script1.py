import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

try:
    cursor.execute("""
        ALTER TABLE orders
        ADD COLUMN phone TEXT
    """)
    print("phone column added successfully.")
except Exception as e:
    print(e)

conn.commit()
conn.close()
