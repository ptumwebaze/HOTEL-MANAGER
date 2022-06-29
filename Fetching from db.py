import sqlite3

connt = sqlite3.connect('customers.db')
cursor = connt.cursor()
cursor.execute('SELECT * FROM customers')
for row in cursor.fetchall():
        print(row)
