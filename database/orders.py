import sqlite3


def save_order(customer_name, phone, order_type, payment_method, table_number, total_amount, cart_items):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO orders(
        customer_name,
        phone,
        order_type,
        payment_method,
        table_number,
        total_amount,
        status
    )
    VALUES(?,?,?,?,?,?,?)

    """, (
        customer_name,
        phone,
        order_type,
        payment_method,
        table_number,
        total_amount,
        "Pending"
    ))

    order_id = cursor.lastrowid

    for item in cart_items:

        cursor.execute("""

            INSERT INTO order_items(

                order_id,

                dish_name,

                quantity,

                price

            )

            VALUES(?,?,?,?)

        """, (
            order_id,
            item["dish_name"],
            item["quantity"],
            item["price"]
        ))

    conn.commit()
    conn.close()

    return order_id


def get_all_orders():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM orders

        ORDER BY order_date DESC

    """)

    orders = cursor.fetchall()

    conn.close()

    return orders

def update_order_status(order_id, status):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        UPDATE orders

        SET status = ?

        WHERE id = ?

    """, (status, order_id))

    conn.commit()

    conn.close()


def get_total_sales():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT SUM(total_amount)

        FROM orders

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0


def get_total_orders():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT COUNT(*)

        FROM orders

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


import sqlite3


def get_order(order_id):

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM orders WHERE id = ?",
        (order_id,)
    )

    order = cursor.fetchone()

    conn.close()

    return order


def get_order_items(order_id):

    import sqlite3

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM order_items

        WHERE order_id = ?

    """, (order_id,))

    items = cursor.fetchall()

    conn.close()

    return items

def delete_order(order_id):

    import sqlite3

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    # Delete all order items first
    cursor.execute(
        "DELETE FROM order_items WHERE order_id=?",
        (order_id,)
    )

    # Delete order
    cursor.execute(
        "DELETE FROM orders WHERE id=?",
        (order_id,)
    )

    conn.commit()

    conn.close()



def get_order_status_counts():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT status, COUNT(*)

        FROM orders

        GROUP BY status

    """)

    rows = cursor.fetchall()

    conn.close()

    counts = {

        "Pending": 0,

        "Preparing": 0,

        "Ready": 0,

        "Served": 0

    }

    for status, total in rows:

        counts[status] = total

    return counts



def get_weekly_sales():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            strftime('%w', order_date),

            SUM(total_amount)

        FROM orders

        GROUP BY strftime('%w', order_date)

    """)

    rows = cursor.fetchall()

    conn.close()

    sales = [0, 0, 0, 0, 0, 0, 0]

    for day, amount in rows:

        sales[int(day)] = amount if amount else 0

    return sales


def get_order_by_id(order_id):

    conn = sqlite3.connect("database.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM orders

        WHERE id = ?

    """, (order_id,))

    order = cursor.fetchone()

    conn.close()

    return order



