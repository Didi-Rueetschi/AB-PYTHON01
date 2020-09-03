import sqlite3

# Connection, Cursor
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# SQL-Queries

#
sql = "SELECT name, firstname FROM personel"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# where-Clause with a condition
sql = "SELECT * FROM personel " \
      "WHERE salary > 3600"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[3])
print()

#
sql = "SELECT * FROM personel " \
      "WHERE name = 'Schmitz'"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

#
sql = "SELECT * FROM personel " \
      "WHERE salary >= 3600 AND salary <= 3650"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[3])

# close the connection
connection.close()

