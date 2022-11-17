import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH=os.path.join(BASE_DIR, 'flower_store', 'database', 'db.sqlite3')
print(DB_PATH)
