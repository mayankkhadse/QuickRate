import os
import sqlite3
import numpy as np
from services.vision_service import get_embedding

DB_PATH = "database/inventory.db"

UPLOAD_DIR = "uploads"
EMBEDDING_DIR = "embeddings"

os.makedirs(EMBEDDING_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("📦 Fetching products from database...")

cursor.execute("SELECT id, product_name, image_path FROM products")
products = cursor.fetchall()

if not products:
    print("❌ No products found in database")
    exit()

count = 0

for product_id, name, image_path in products:

    try:
        if not image_path:
            print(f"⚠️ Skipping {name} (no image)")
            continue

        full_path = image_path

        # If only filename stored, fix path
        if not os.path.exists(full_path):
            full_path = os.path.join(UPLOAD_DIR, image_path)

        if not os.path.exists(full_path):
            print(f"⚠️ Image not found for {name}: {full_path}")
            continue

        print(f"🔄 Processing {name}...")

        embedding = get_embedding(full_path)

        np.save(
            os.path.join(EMBEDDING_DIR, f"{name}.npy"),
            embedding
        )

        count += 1

        print(f"✅ Done: {name}")

    except Exception as e:
        print(f"❌ Failed for {name}: {e}")

print(f"\n🎯 Migration completed: {count} products converted into embeddings")