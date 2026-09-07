import sqlite3


def check_admin(username, password):

    conn = sqlite3.connect("database.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM admins

        WHERE username = ?

        AND password = ?

    """, (username, password))

    admin = cursor.fetchone()

    conn.close()

    return admin


def create_default_admin():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM admins

    """)

    admin = cursor.fetchone()

    if not admin:

        cursor.execute("""

            INSERT INTO admins(

                username,

                password

            )

            VALUES(?,?)

        """, (

            "admin",

            "admin123"

        ))

    conn.commit()

    conn.close()