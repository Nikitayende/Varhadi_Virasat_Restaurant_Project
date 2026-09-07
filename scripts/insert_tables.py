import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

tables = []

# Dining (1-15)
for i in range(1, 16):
    tables.append((
        i,
        "Dining",
        f"D{i}",
        f"images/table_qr/table_{i}.png",
        "Available"
    ))

# Private Dining (16-20)
for i in range(16, 21):
    tables.append((
        i,
        "Private Dining",
        f"P{i-15}",
        f"images/table_qr/table_{i}.png",
        "Available"
    ))

# Terrace (21-25)
for i in range(21, 26):
    tables.append((
        i,
        "Terrace",
        f"T{i-20}",
        f"images/table_qr/table_{i}.png",
        "Available"
    ))

# Garden (26-30)
for i in range(26, 31):
    tables.append((
        i,
        "Garden",
        f"G{i-25}",
        f"images/table_qr/table_{i}.png",
        "Available"
    ))

for table in tables:
    try:
        cursor.execute("""
            INSERT INTO restaurant_tables
            (
                table_number,
                area,
                position,
                qr_code,
                status
            )
            VALUES (?, ?, ?, ?, ?)
        """, table)
    except sqlite3.IntegrityError:
        print(f"Table {table[0]} already exists.")

conn.commit()
conn.close()

print("All restaurant tables inserted successfully!")