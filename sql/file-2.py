import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# SELECT.
cur.execute('SELECT Region, Population FROM PopByRegion')
print(cur.fetchone())
print(cur.fetchall())

# ORDER BY.
cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
print(cur.fetchall())

cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Population')
print(cur.fetchall())

# SELECT ALL.
cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())

