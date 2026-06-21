import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

conn = sqlite3.connect("database/inventory.db")

df = pd.read_sql_query("SELECT * FROM products", conn)

if len(df) < 5:
    print("Not enough data")
    exit()

df["branch"] = df["branch"].astype("category").cat.codes

X = df[["buy_price", "quantity", "branch"]]
y = df["sell_price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

with open("ml/price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully")