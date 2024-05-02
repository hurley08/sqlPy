# db.py

import sqlite3

conn = sqlite3.connect("legos.db")

c = conn.cursor()