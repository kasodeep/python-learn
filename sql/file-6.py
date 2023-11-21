import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

cur.execute('CREATE TABLE PopByRegion (id INTEGER, Region TEXT, Population INTEGER)')
cur.execute('INSERT INTO PopByRegion VALUES (?, ?, ?)', (2, "Goa", 80000))

# List of entries.
cities = [
   (1, "Mumbai", "Gate of India"),
   (5, "Varanasi", "Kashi Vishwanath Temple"),
   (4, "Ujjain", "Kalbhairavnath Temple"),
   (3, "Kevadiya", "Statue of Unity"),
   (1, "Pune", "Shivneri")
]

# Creating new table.
cur.execute('CREATE TABLE PopByCity (id INTEGER, City TEXT, Landmark TEXT)')

# Entering the entires.
for c in cities:
	cur.execute('INSERT INTO PopByCity VALUES(?, ?, ?)', (c[0], c[1], c[2]))

# Commiting the changes.
con.commit()

cur.execute('SELECT * FROM PopByCity')
print(cur.fetchall())