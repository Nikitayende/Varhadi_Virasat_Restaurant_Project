import sqlite3


def get_all_tables():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM restaurant_tables
        ORDER BY table_number
    """)

    tables = cursor.fetchall()

    conn.close()

    return tables


def get_table(table_id):

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM restaurant_tables
        WHERE id=?
    """, (table_id,))

    table = cursor.fetchone()

    conn.close()

    return table


def update_table_status(table_id, status):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE restaurant_tables
        SET status=?
        WHERE id=?
    """, (status, table_id))

    conn.commit()

    conn.close()


def get_table_stats():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT area, COUNT(*)
        FROM restaurant_tables
        GROUP BY area
    """)

    stats = cursor.fetchall()

    conn.close()

    return stats

import qrcode

BASE_URL = "http://192.168.31.176:5000/table"


def add_table(table_number, area, position):

    qr_path = f"static/images/table_qr/table_{table_number}.png"

    qr = qrcode.make(f"{BASE_URL}/{table_number}")

    qr.save(qr_path)

    db_path = f"images/table_qr/table_{table_number}.png"

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO restaurant_tables
        (
            table_number,
            area,
            position,
            qr_code,
            status
        )
        VALUES(?,?,?,?,?)
    """,
    (
        table_number,
        area,
        position,
        db_path,
        "Available"
    ))

    conn.commit()
    conn.close()

def delete_table(table_id):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM restaurant_tables WHERE id=?",
        (table_id,)
    )

    conn.commit()

    conn.close()
    
