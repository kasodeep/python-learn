import tkinter as tk
from tkinter import messagebox
import sqlite3
from main import *

# SQLite database setup.
conn = sqlite3.connect('hotel.db')
c = conn.cursor()

# Create a table if not exists.
c.execute('''
          CREATE TABLE IF NOT EXISTS customers (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              number INTEGER NOT NULL,
              email TEXT UNIQUE NOT NULL
          )
          ''')
conn.commit()

# Function to add a new customer to the database.
def add_customer():
    name = name_entry.get()
    email = email_entry.get()
    number = number_entry.get()

    # Check if email is unique.
    c.execute('SELECT * FROM customers WHERE email = ?', (email,))
    if c.fetchone():
        messagebox.showerror('Error', 'Email must be unique')
        return

    # Insert new customer into the database.
    c.execute('INSERT INTO customers (name, number, email) VALUES (?, ?, ?)', (name, number, email))
    conn.commit()

    messagebox.showinfo('Success', 'Customer added successfully')

# Function to search for a customer by email or ID.
def search_customer():
    search_value = search_entry.get()
    search_by = search_by_var.get()

    if search_by == 'Email':
        c.execute('SELECT * FROM customers WHERE email = ?', (search_value,))
    else:
        c.execute('SELECT * FROM customers WHERE id = ?', (search_value,))
    result = c.fetchone()

    if result:
        customer_data = [(result[0], result[1], result[2], result[3])]
        info_window = Main(customer_data)
        info_window.mainloop()
    else:
        messagebox.showinfo('Result', 'Customer not found')

# Tkinter GUI setup.
root = tk.Tk()

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size to half of the screen size
window_width = int(screen_width / 2)
window_height = int(screen_height / 2)

# Set the window size and position it in the center
root.geometry(f'{window_width}x{window_height}')
root.title('Hotel Login')

# Frame for adding a new customer
frame_add_customer = tk.LabelFrame(root, text='Add Customer', font=('Space Mono', 14, 'bold'), padx=10, pady=10)
frame_add_customer.pack(pady=10)

tk.Label(frame_add_customer, text='Name:').grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame_add_customer)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_add_customer, text='Number:').grid(row=1, column=0, padx=5, pady=5)
number_entry = tk.Entry(frame_add_customer)
number_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_add_customer, text='Email:').grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(frame_add_customer)
email_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(frame_add_customer, text='Add Customer', command=add_customer)
add_button.grid(row=3, column=0, columnspan=2, pady=10)


# Frame for searching a customer.
frame_search_customer =  tk.LabelFrame(root, text='Search Customer', font=('Helvetica', 14, 'bold'), padx=10, pady=10)
frame_search_customer.pack(pady=10)

tk.Label(frame_search_customer, text='Search By:').grid(row=0, column=0, padx=5, pady=5)
search_by_var = tk.StringVar()
search_by_var.set('Email')

# Searching Options.
search_by_menu = tk.OptionMenu(frame_search_customer, search_by_var, 'Email', 'ID')
search_by_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_search_customer, text='Search Value:').grid(row=1, column=0, padx=5, pady=5)
search_entry = tk.Entry(frame_search_customer)
search_entry.grid(row=1, column=1, padx=5, pady=5)

search_button = tk.Button(frame_search_customer, text='Search Customer', command=search_customer)
search_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Application.
root.mainloop()
conn.close()
