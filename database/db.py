import sqlite3

conn = sqlite3.connect("database/inventory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    buy_price REAL,
    sell_price REAL,
    quantity INTEGER,
    branch TEXT,
    image_path TEXT
)
""")

conn.commit()