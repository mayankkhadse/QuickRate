import sqlite3

conn = sqlite3.connect("database/inventory.db", check_same_thread=False)
cursor = conn.cursor()

def add_product(name, buy, sell, qty, branch, image_path):
    cursor.execute("""
        INSERT INTO products(
            product_name, buy_price, sell_price, quantity, branch, image_path
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (name, buy, sell, qty, branch, image_path))
    conn.commit()


def get_all():
    return cursor.execute("SELECT * FROM products").fetchall()


def delete_product(pid):
    cursor.execute("DELETE FROM products WHERE id=?", (pid,))
    conn.commit()