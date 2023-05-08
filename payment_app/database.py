import sqlite3

conn = sqlite3.connect('recovered_text.db')
cursor = conn.cursor()

# Select the last row from the table and print the result
cursor.execute('SELECT * FROM recovered_text ORDER BY id DESC LIMIT 1')
row = cursor.fetchone()
print(row[1])


conn.close()
