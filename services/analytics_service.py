import sqlite3

def get_dashboard_stats():
    conn = sqlite3.connect("database/inventory.db", check_same_thread=False)
    cursor = conn.cursor()

    total = cursor.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    stock = cursor.execute("SELECT SUM(quantity) FROM products").fetchone()[0] or 0
    profit = cursor.execute("""
        SELECT SUM((sell_price - buy_price) * quantity)
        FROM products
    """).fetchone()[0] or 0

    return {
        "products": total,
        "stock": stock,
        "profit": profit
    }

def stats():
    return get_dashboard_stats()
