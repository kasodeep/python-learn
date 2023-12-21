import sqlite3

conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()

def add_stat(item, quantity):
    cursor.execute('''INSERT INTO stats(item, quantity) VALUES(?, ?)''', (item, quantity))
    conn.commit()

def main():
    cursor.execute('''CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, quantity INTEGER, date DATE DEFAULT CURRENT_DATE, FOREIGN KEY (item) REFERENCES menu(name))''')
    conn.commit()

def search_by_date(date):
    cursor.execute("SELECT item, quantity FROM stats WHERE date=?", (date,))
    data = cursor.fetchall()
    return data

def print_data():
    cursor.execute("SELECT * FROM stats, menu WHERE stats.item = menu.name")
    result = cursor.fetchall()
    print(result)

if __name__ == "__main__":
    cursor.execute("DROP TABLE stats")
    conn.commit()
    
    main()
    print_data()
    conn.close()
   