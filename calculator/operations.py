from tkinter import messagebox
import math

def add_to_expression(self, value):
   self.current_expression += str(value)
   self.update_label()

def append_operator(self, operator):
   self.current_expression += operator
   self.total_expression += self.current_expression
   self.current_expression = ""
   self.update_total_label()
   self.update_label()

def evaluate(self):
   self.total_expression += self.current_expression
   self.update_total_label()
   try:
      self.current_expression = str(eval(self.total_expression))
      self.total_expression = ""
   except Exception as e:
      clear(self)
      messagebox.showinfo("Warning", e)
   self.update_label()

def square(self):
    try:
        self.current_expression = str(eval(f'{self.current_expression}**2'))
    except Exception as e:
        clear(self)
        messagebox.showinfo("Warning", e)
    self.update_label()

def sqrt(self):
    try:
        self.current_expression = str(eval(f'{self.current_expression}**0.5'))
    except Exception as e:
        clear(self)
        messagebox.showinfo("Warning", e)
    self.update_label()

def back(self):
    if len(self.current_expression) != 0:
        self.current_expression = self.current_expression[:-1]
        self.update_label()
        
def clear(self):
    self.current_expression = ""
    self.total_expression = ""
    self.update_label()
    self.update_total_label()

def change_sign(self):
    if self.current_expression[:1] == "-":
        self.current_expression = self.current_expression[1:]
    else:
        self.current_expression = '-' + self.current_expression
    self.update_label()

def inverse(self):
    try:
        self.current_expression = str(eval(f'1/{self.current_expression}'))
    except Exception as e:
        clear(self)
        messagebox.showinfo("Warning", e)
    self.update_label()

def trigo(select, self):
    try:
        if select == "sin":
            self.current_expression = str(math.sin(eval(self.current_expression)))
        elif select == "cos":
            self.current_expression = str(math.cos(eval(self.current_expression)))
        elif select == "tan":
            self.current_expression = str(math.tan(eval(self.current_expression)))
        elif select == "sinh":
            self.current_expression = str(math.sinh(eval(self.current_expression)))
        elif select == "cosh":
            self.current_expression = str(math.cosh(eval(self.current_expression)))
        elif select == "tanh":
            self.current_expression = str(math.tanh(eval(self.current_expression)))
        self.update_label()
    except Exception as e:
        clear(self)
        messagebox.showinfo("Warning", e)

def log(select, self):
    try:
        if select == "e^x":
            self.current_expression = str(math.pow(math.e, eval(self.current_expression)))
        elif select == "e":
            self.current_expression = str(math.e)
        elif select == "PI":
            self.current_expression = str(math.pi)
        elif select == "10^x":
            self.current_expression = str(math.pow(10, eval(self.current_expression)))
        self.update_label()
    except Exception as e:
        clear(self)
        messagebox.showinfo("Warning", e)