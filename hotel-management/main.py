from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk
from datetime import date
from menu import *
import random
from stats import *

class Main(tk.Toplevel):
    # Init Function.
    def __init__(self, customer_data):
        super().__init__()
        
        self.title(customer_data[0][1])
        self.geometry("1050x600")
        self.customer_data = customer_data
        
        # Frame for drops.
        self.menu_frame = tk.LabelFrame(self, text='Menu Options', font=('Space Mono', 14), padx=10, pady=10)
        self.menu_frame.pack(side="left")
        self.create_menu_frame()
        
        # Frame for Table And Pie Chart.
        self.main_frame = tk.Label(self, font=('Space Mono', 14))
        self.main_frame.pack(side="left")
        
        # Table for Order.
        self.order_table = tk.LabelFrame(self.main_frame, text='Order Summary', font=('Space Mono', 14))
        self.order_table.pack(side="top")

        # Order Info.
        self.order = []
        self.tree = self.create_order_table()
        
        # Statistics Info.
        self.statistics = tk.LabelFrame(self.main_frame, text='Statistics', font=('Space Mono', 14), padx=10, pady=10)
        self.statistics.pack(side="bottom", expand=True, fill='both')  

        # Date Selection 
        self.cal = DateEntry(self.statistics, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.cal.grid(row=0, column=0, padx=10, pady=10)        
        self.cal.bind("<<DateEntrySelected>>", self.show_stats)
        
    def add_to_order(self, quantity, selected):
        item = search_menu_item(selected)
        item = (item[0], quantity, item[1], quantity * item[1])
        
        self.order.append(item)
        self.tree.insert('', 'end', values=item)

    def delete_item(self):
        selected = self.tree.selection()[0]
        if selected is None: return
        
        index = selected[-1]
        self.order.pop(int(index) - 1)
        self.tree.delete(selected)
    
    # Creates basic table structure.
    def create_order_table(self):
        # TreeView
        tree = ttk.Treeview(self.order_table, columns=('Name', 'Quantity', 'Price', 'Total'), show='headings')
        tree.heading('Name', text='Name')
        tree.heading('Quantity', text='Quantity')
        tree.heading('Price', text='Price')
        tree.heading('Total', text='Total')
        tree.pack(expand=True, fill='both')

        # Options
        button = tk.Button(self.order_table, text = "Generate Bill", command=self.print_bill)
        button.pack(expand=True, fill='both')
        delete = tk.Button(self.order_table, text = "Delete Item", command=lambda: self.delete_item())
        delete.pack(expand=True, fill='both')
        return tree

    # For Creating Option Menu.
    def create_menu_frame(self):
        
        # Top Frame
        frame = tk.LabelFrame(self.menu_frame, text='Regular', font=('Space Mono', 14), padx=30, pady=10)
        frame.pack(padx=10, pady=10)
        regular = get_items_by_category("REGULAR")        
  
        r_selected = tk.StringVar() 
        r_selected.set(regular[0]) 
  
        drop = tk.OptionMenu(frame, r_selected , *regular ) 
        drop.grid(row=0, column=0, sticky=tk.NSEW)
        
        r_quantity = tk.IntVar()
        r_slider = tk.Scale(frame, variable = r_quantity, from_ = 1, to = 10, orient = tk.HORIZONTAL) 
        r_slider.grid(row=1, column=0, sticky=tk.NSEW)

        r_button = tk.Button( frame, text = "Add To Order", command=lambda: self.add_to_order(r_quantity.get(), r_selected.get()))
        r_button.grid(row=2, column=0, sticky=tk.NSEW)

        # Middle Frame
        frame = tk.LabelFrame(self.menu_frame, text='Special', font=('Space Mono', 14), padx=30, pady=10)
        frame.pack(padx=10, pady=10)
        special = get_items_by_category("SPECIAL")        
  
        s_selected = tk.StringVar() 
        s_selected.set(special[0]) 
  
        drop = tk.OptionMenu(frame, s_selected , *special ) 
        drop.grid(row=0, column=0, sticky=tk.NSEW)
        
        s_quantity = tk.IntVar()
        s_slider = tk.Scale(frame, variable = s_quantity, from_ = 1, to = 10, orient = tk.HORIZONTAL) 
        s_slider.grid(row=1, column=0, sticky=tk.NSEW)

        s_button = tk.Button( frame, text = "Add To Order", command=lambda: self.add_to_order(s_quantity.get(), s_selected.get()))
        s_button.grid(row=2, column=0, sticky=tk.NSEW)
        
        # Bottom Frame
        frame = tk.LabelFrame(self.menu_frame, text='Beverages', font=('Space Mono', 14), padx=30, pady=10)
        frame.pack(padx=10, pady=10)
        drinks = get_items_by_category("DRINKS")
  
        d_selected = tk.StringVar() 
        d_selected.set(drinks[0]) 
  
        drop = tk.OptionMenu(frame, d_selected , *drinks ) 
        drop.grid(row=0, column=0, sticky=tk.NSEW)
        
        d_quantity = tk.IntVar()
        d_slider = tk.Scale( frame, variable = d_quantity, from_ = 1, to = 10, orient = tk.HORIZONTAL) 
        d_slider.grid(row=1, column=0, sticky=tk.NSEW)

        d_button = tk.Button( frame, text = "Add To Order", command=lambda: self.add_to_order(d_quantity.get(), d_selected.get()))
        d_button.grid(row=2, column=0, sticky=tk.NSEW)
               
    def print_bill(self):
        # Create the main window
        root = tk.Tk()
        root.title("Bill")

        # Create a Text widget for displaying the bill
        bill_text = tk.Text(root, height=20, width=40)
        bill_text.pack()

        # Add bill header
        bill_text.insert(tk.END, "----Night Coders Hotel----\n")
        bill_text.insert(tk.END, "       BILL\n")
        bill_text.insert(tk.END, "----------------------\n")
        bill_text.insert(tk.END, "\n")
        
        bill_text.insert(tk.END, f"Id: {self.customer_data[0][0]}\n")
        bill_text.insert(tk.END, f"Name: {self.customer_data[0][1]}\n")
        bill_text.insert(tk.END, f"Contact No: {self.customer_data[0][2]}\n")
        bill_text.insert(tk.END, f"Email: {self.customer_data[0][3]}\n")
        
        # Add item details to the bill
        for item in self.order:
            name, quantity, price, total = item
            line = f"{name}  \u20b9{price}  x{quantity:.2f}  Total: \u20b9{total:.2f}\n"
            bill_text.insert(tk.END, line)        

        # Add bill footer
        bill_text.insert(tk.END, "----------------------\n")

        # Calculate and display the total amount
        total_amount = sum(item[3] for item in self.order)
        bill_text.insert(tk.END, f"Total Amount: \u20b9{total_amount:.2f}\n")
        
        # Add a button to save the bill to a text file
        save_button = tk.Button(root, text="Save Bill", command=lambda: self.save_bill_to_file(root))
        save_button.pack()

        # Run the Tkinter main loop
        root.mainloop()
    
    def save_bill_to_file(self, root):
        file_name = f"{self.customer_data[0][1] + str(random.randint(0, 999))}.txt"

        with open(file_name, "w") as file:
            # Write bill header
            file.write("----Night Coders Hotel----\n")
            file.write("       BILL\n")
            file.write("----------------------\n")
            file.write(f"Id: {self.customer_data[0][0]}\n")
            file.write(f"Name: {self.customer_data[0][1]}\n")
            file.write(f"Contact No: {self.customer_data[0][2]}\n")
            file.write(f"Email: {self.customer_data[0][3]}\n")

            # Write item details to the file
            for item in self.order:
                name, quantity, price, total = item
                line = f"{name}  ${price}  x{quantity:.2f}  Total: ${total:.2f}\n"
                file.write(line)
                add_stat(name, quantity)

            # Write bill footer
            file.write("----------------------\n")

            # Calculate and write the total amount
            total_amount = sum(item[3] for item in self.order)
            file.write(f"Total Amount: ${total_amount:.2f}\n")        
            
            root.destroy()
            self.options = []
            self.show_stats(date.today())
            self.tree.delete(*self.tree.get_children())

    def show_stats(self, event):
        data = search_by_date(self.cal.get_date())
        items = [record[0] for record in data]
        quantities = [record[1] for record in data]

        # Create a pie chart
        fig = Figure(figsize=(3, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(quantities, labels=items, autopct='%1.1f%%', startangle=90)

        # Embed the matplotlib figure in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.statistics)
        canvas.get_tk_widget().grid(row=0, column=1)       
