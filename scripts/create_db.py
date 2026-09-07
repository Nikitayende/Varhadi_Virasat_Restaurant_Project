import sqlite3

# Connect to SQLite
conn = sqlite3.connect("database.db")

cursor = conn.cursor()

# ==========================
# ADMIN TABLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS admins(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL,

    password TEXT NOT NULL

)
""")

# ==========================
# MENU CATEGORIES
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    category_name TEXT NOT NULL

)
""")

# ==========================
# MENU ITEMS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_items(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    dish_name TEXT NOT NULL,

    category TEXT NOT NULL,

    sub_category TEXT,

    price REAL,

    image TEXT,

    description TEXT,

    available TEXT DEFAULT 'Yes',

    special TEXT DEFAULT 'No',

    rating REAL

)
""")

# ==========================
# RESTAURANT TABLES
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurant_tables(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    table_number INTEGER UNIQUE,

    area TEXT,

    position TEXT,

    qr_code TEXT,

    status TEXT DEFAULT 'Available'

)
""")

# ==========================
# CUSTOMERS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    customer_name TEXT,

    phone TEXT

)
""")

# ==========================
# CART
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS cart(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    dish_id INTEGER,

    quantity INTEGER

)
""")

# ==========================
# ORDERS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    customer_name TEXT,

    table_number INTEGER,

    total_amount REAL,

    status TEXT,

    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# ==========================
# ORDER ITEMS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    order_id INTEGER,

    dish_name TEXT,

    quantity INTEGER,

    price REAL

)
""")

# ==========================
# RESERVATIONS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservations(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    phone TEXT,

    reservation_date TEXT,

    reservation_time TEXT,

    guests INTEGER,
               
    status TEXT DEFAULT 'Pending'

)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")


