import sqlite3

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("SELECT * FROM reservations")

rows = cursor.fetchall()

if len(rows) == 0:

    print("No reservations found.")

else:

    print("\n===== RESERVATIONS =====\n")

    for row in rows:

        print(f"ID: {row['id']}")
        print(f"Name: {row['name']}")
        print(f"Phone: {row['phone']}")
        print(f"Date: {row['reservation_date']}")
        print(f"Time: {row['reservation_time']}")
        print(f"Guests: {row['guests']}")
        print("-" * 40)

conn.close()