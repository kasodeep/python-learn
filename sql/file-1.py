import sqlite3

# Connects if database is available else creates the database.
con = sqlite3.connect('populatiton.db')

# Pointer to the database.
cur = con.cursor()

# Creating a table.
cur.execute("CREATE TABLE PopByRegion (Id INTEGER, Region TEXT, Population INTEGER)")

# Inserting the values into the table.
cur.execute('INSERT INTO PopByRegion VALUES(1, "Maharashtra", NULL)')
cur.execute('INSERT INTO PopByRegion VALUES(2, "Goa", 80000)')
cur.execute('INSERT INTO PopByRegion VALUES(3, "Gujrat", 2000000)')
cur.execute('INSERT INTO PopByRegion VALUES(?, ?, ?)', (4, "MP", 2000000))
cur.execute('INSERT INTO PopByRegion VALUES(?, ?, ?)', (5, "UP", 10000000))

# Commiting the changes.
con.commit()
