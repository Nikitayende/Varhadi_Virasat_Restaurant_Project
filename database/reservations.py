import sqlite3


def save_reservation(
    name,
    phone,
    reservation_date,
    reservation_time,
    guests
):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO reservations(

            name,

            phone,

            reservation_date,

            reservation_time,

            guests

        )

        VALUES(?,?,?,?,?)

    """, (

        name,

        phone,

        reservation_date,

        reservation_time,

        guests

    ))

    conn.commit()

    conn.close()


def get_all_reservations():

    conn = sqlite3.connect("database.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM reservations

        ORDER BY reservation_date,
                 reservation_time

    """)

    reservations = cursor.fetchall()

    conn.close()

    return reservations


def delete_reservation(reservation_id):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        DELETE FROM reservations

        WHERE id = ?

    """, (reservation_id,))

    conn.commit()

    conn.close()


def get_total_reservations():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT COUNT(*)

        FROM reservations

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def update_reservation_status(reservation_id, status):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        UPDATE reservations

        SET status = ?

        WHERE id = ?

    """, (

        status,

        reservation_id

    ))

    conn.commit()

    conn.close()




    