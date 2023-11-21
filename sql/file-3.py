import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# COMPARISONS.
cur.execute('SELECT Region FROM PopByRegion WHERE Population > 200000')
print(cur.fetchall())

cur.execute('SELECT Region FROM PopByRegion WHERE Population < 200000')
print(cur.fetchall())

cur.execute('SELECT Region FROM PopByRegion WHERE Population > 20000 AND Region = "MP"')
print(cur.fetchall())