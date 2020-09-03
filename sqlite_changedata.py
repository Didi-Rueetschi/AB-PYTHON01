import sqlite3

def Message():
    #
    sql = "SELECT * FROM personel"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()

# Verbindung, Cursor
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# Before
Message()

# update the recordset
sql = "UPDATE personel SET salary = 3780 " \
      "WHERE personnalnumber = 81343"
cursor.execute(sql)
connection.commit()

# After
Message()

connection.close()

