import sqlite3
conn = sqlite3.connect('college.db')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(event)")
for column in cursor.fetchall():
    print(column)
conn.close()
