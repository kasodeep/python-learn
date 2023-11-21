import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# Delete the Table.
cur.execute('DROP TABLE PopByRegion')