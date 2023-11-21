import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# INNER JOIN
cur.execute('SELECT PopByRegion.Region, PopByCity.City FROM PopByRegion INNER JOIN PopByCity WHERE (PopByRegion.Id = PopByCity.ID)')
print(cur.fetchall())
