import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# WHERE.
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Goa"')
print(cur.fetchone())

# UPDATE.
cur.execute('UPDATE PopByRegion SET Population = 10000 WHERE Region = "Goa"')

# CHECK.
cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())

# DELETE.
cur.execute('DELETE FROM PopByRegion WHERE Region = "Goa"')

# CHECK.
cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())