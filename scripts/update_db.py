import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

try:
    cursor.execute("""
        ALTER TABLE orders
        ADD COLUMN order_type TEXT DEFAULT 'Dine In'
    """)
    print("✅ order_type column added successfully.")

except sqlite3.OperationalError as e:
    print("⚠️", e)

conn.commit()
conn.close()