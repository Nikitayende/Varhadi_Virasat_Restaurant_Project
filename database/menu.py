import sqlite3


def get_all_menu_items():

    conn = sqlite3.connect("database.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM menu_items

        ORDER BY category, dish_name

    """)

    menu_items = cursor.fetchall()

    conn.close()

    return menu_items

def add_menu_item(dish_name,
                  category,
                  price,
                  image,
                  description):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO menu_items(

            dish_name,

            category,

            price,

            image,

            description

        )

        VALUES(?,?,?,?,?)

    """,(
        dish_name,
        category,
        price,
        image,
        description
    ))

    conn.commit()

    conn.close()

def get_menu_item(item_id):

    conn = sqlite3.connect("database.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM menu_items

        WHERE id = ?

    """, (item_id,))

    item = cursor.fetchone()

    conn.close()

    return item

def update_menu_item(
    item_id,
    dish_name,
    category,
    price,
    image,
    description
):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        UPDATE menu_items

        SET

            dish_name = ?,

            category = ?,

            price = ?,

            image = ?,

            description = ?

        WHERE id = ?

    """, (

        dish_name,

        category,

        price,

        image,

        description,

        item_id

    ))

    conn.commit()

    conn.close()

def get_special_dishes():

    conn = sqlite3.connect("database.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM menu_items

        ORDER BY rating DESC, dish_name

        LIMIT 6

    """)

    dishes = cursor.fetchall()

    conn.close()

    return dishes

def delete_menu_item(item_id):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        DELETE FROM menu_items

        WHERE id = ?

    """, (item_id,))

    conn.commit()

    conn.close()


def get_total_menu_items():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT COUNT(*)

        FROM menu_items

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total








