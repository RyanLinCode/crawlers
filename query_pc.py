import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='pchome')
cursor = cnx.cursor(dictionary=True)

query = ("SELECT * FROM products "
         "WHERE name LIKE '%msi%'")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)

for row in cursor:
  print(row)

cursor.close()
cnx.close()