import sqlite3

def Message():
    # SQL-Abfrage, senden, Message
    sql = "SELECT * FROM personel"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()

# Verbindung, Cursor
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# Vorher
Message()

# Datensatz entfernen
sql = "DELETE FROM personel " \
      "WHERE personnalnumber = 8339"
cursor.execute(sql)
connection.commit()

# Nachher
Message()

connection.close()

