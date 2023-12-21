import sqlite3

conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()

# Function to create a new menu item
def add_menu_item(name, price, category):

    # Check if the item already exists
    cursor.execute("SELECT * FROM menu WHERE name=?", (name,))
    existing_item = cursor.fetchone()

    if existing_item:
        print("Item with this name already exists. Please choose a different name.")
        return

    # Insert the new item into the menu table
    cursor.execute("INSERT INTO menu (name, price, category) VALUES (?, ?, ?)", (name, price, category))
    conn.commit()
    print("Menu item added successfully.")

# Function to search for a menu item by name
def search_menu_item(name):
    cursor = conn.cursor()

    # Search for the item by name
    cursor.execute("SELECT * FROM menu WHERE name=?", (name,))
    result = cursor.fetchone()

    if result:
        return [result[0], result[1]]
    else:
        print("Menu item not found.")

# Function to get a list of items grouped by category
def get_items_by_category(category):
    
    # Search for items in the specified category
    cursor.execute("SELECT * FROM menu WHERE category=?", (category,))
    items = cursor.fetchall()
    list = []

    if items:
        for item in items:
            list.append(item[0])
        return list
    else:
        print(f"No items found in the category '{category}'.")


# Main function to create the menu database and demonstrate the functions
def main():
    # Connect to the SQLite database (or create it if it doesn't exist)

    # Create a menu table if it doesn't exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            name TEXT PRIMARY KEY,
            price REAL,
            category TEXT
        )
    ''')

    while(True):
        name = input("Enter Name:")
        price = input("Enter Price:")
        category = input("Enter Category:")
        
        cursor.execute("INSERT INTO menu (name, price, category) VALUES (?, ?, ?)", (name, price, category))
        conn.commit()
        print("Menu item added successfully.")

    # Close the database connection when done
    conn.close()

if __name__ == "__main__":
    main()