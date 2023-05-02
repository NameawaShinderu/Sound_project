import sqlite3

conn = sqlite3.connect('recovered_text.db')
cursor = conn.cursor()

# Select all rows from the table and print the results
cursor.execute('SELECT * FROM recovered_text')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
