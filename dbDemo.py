import mysql.connector

from utilities.config import getconnection

conn = getconnection()


print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
# print(row)
row_all = cursor.fetchall()
print(row_all)

for row in row_all:
    print(row[2])

query = 'update customerInfo set Location = %s where CourseName = %s'
data = ("England","Jmeter")
cursor.execute(query,data)
conn.commit()