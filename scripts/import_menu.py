import sqlite3
import pandas as pd

# Read Excel file
df = pd.read_excel("menu_data.xlsx")

# Rename columns
df.rename(columns={
    "ID": "id",
    "Dish Name": "dish_name",
    "Category": "category",
    "Sub Category": "sub_category",
    "Price": "price",
    "Image": "image",
    "Description": "description",
    "Available": "available",
    "Special": "special",
    "Rating": "rating"
}, inplace=True)

# Clean price column
df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
).fillna(0)

# Connect to database
conn = sqlite3.connect("database.db")

cursor = conn.cursor()

# Delete old menu
cursor.execute("DELETE FROM menu_items")

conn.commit()

# Import new menu
df.to_sql(
    "menu_items",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print("✅ Menu Imported Successfully!")