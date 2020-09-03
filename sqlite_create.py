import os, sys, sqlite3


if os.path.exists("company.db"):
    print("Database already exists")
    sys.exit(0)


connection = sqlite3.connect("company.db")


cursor = connection.cursor()

sql = "CREATE TABLE personel(" \
      "name TEXT, " \
      "firstname TEXT, " \
      "personnalnumber INTEGER PRIMARY KEY, " \
      "salary REAL, " \
      "birthday TEXT)"
cursor.execute(sql)

sql = "INSERT INTO personel VALUES('Maier', " \
      "'Hans', 6714, 3500, '15.03.1962')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO personel VALUES('Schmitz', " \
      "'Peter', 81343, 3750, '12.04.1958')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO personel VALUES('Mertens', " \
      "'Julia', 2297, 3621.5, '30.12.1959')"
cursor.execute(sql)
connection.commit()

# Verbindung beenden
connection.close()
