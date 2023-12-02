import tkinter as tk
from operations import *

# Font Styles
SMALL_FONT_STYLE = ("Space Mono", 16)
LARGE_FONT_STYLE = ("Space Mono", 40, "bold")
DIGIT_FONT_STYLE = ("Space Mono", 24, "bold")
DEFAULT_FONT_STYLE = ("Space Mono", 20)

# Colors
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8F8FF"
LIGHT_BLUE = "#CCEDFF"

class Calculator:
   # init function.
   def __init__(self):

      # Root Element.
      self.window = tk.Tk()
      self.window.geometry("325x525")
      self.window.resizable(0, 0)
      self.window.title("Calculator")

      self.total_expression = ""
      self.current_expression = ""

      self.display_frame = self.create_display_frame()
      self.total_label, self.label = self.create_display_labels()
      self.menu_frame = self.create_dropdown_menus()        

      self.digits = {
         7:(2, 1), 8:(2, 2), 9:(2, 3),
         4:(3, 1), 5:(3, 2), 6:(3, 3),
         1:(4, 1), 2:(4, 2), 3:(4, 3),
         0:(5, 2), ".":(5, 3)
      }
      self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

      # Buttons Wiring.
      self.buttons_frame = self.create_buttons_frame()
      for i in range(0, 6):
         self.buttons_frame.rowconfigure(i, weight=1)

      for i in range(1, 5):
         self.buttons_frame.columnconfigure(i, weight=1)

      self.create_digit_buttons()
      self.create_operator_buttons()
      
      # Special Features.
      self.create_special_buttons()
      self.bind_keys()

   # keyboard functionality.
   def bind_keys(self):
      self.window.bind("<Return>", lambda event: evaluate(self))
      self.window.bind("=", lambda event: evaluate(self))

      self.window.bind("<BackSpace>", lambda event: back(self))
      self.window.bind("%", lambda event: append_operator(self, "%"))

      for key in self.digits:
         self.window.bind(str(key), lambda event, digit=key: add_to_expression(self, digit))

      for key in self.operators:
         self.window.bind(key, lambda event, digit=key: append_operator(self, digit))

   # special buttons.
   def create_special_buttons(self):
      self.create_clear_button()
      self.create_equal_button()
      self.create_square_button()
      self.create_sqrt_button()
      self.create_change_sign_button()
      self.create_modulo_button()
      self.create_back_button()
      self.create_inverse_button()

   # frame.
   def create_display_frame(self):
      frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
      frame.pack(expand=True, fill="both")
      return frame
   
   # labels.
   def create_display_labels(self):
      total_label = tk.Label(self.display_frame, text=self.total_expression,
                              anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
      total_label.pack(expand=True, fill="both")

      label = tk.Label(self.display_frame, text=self.current_expression,
                              anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
      label.pack(expand=True, fill="both")

      return total_label, label

   # Buttons Frame.
   def create_buttons_frame(self):
      frame = tk.Frame(self.window)
      frame.pack(expand=True, fill="both")
      return frame
   
   # Digits.
   def create_digit_buttons(self):
      for digit, grid_value in self.digits.items():
         button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                            font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x = digit: add_to_expression(self, x))
         button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

   # Operators.
   def create_operator_buttons(self):
      i = 1
      for operator, symbol in self.operators.items():
         button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x = operator: append_operator(self, x))
         button.grid(row=i, column=4, sticky=tk.NSEW)
         i += 1

   # equals button.
   def create_equal_button(self):
      button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: evaluate(self))
      button.grid(row=5, column=4, sticky=tk.NSEW)

   # sign button.
   def create_change_sign_button(self):
      button = tk.Button(self.buttons_frame, text="+/-", bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: change_sign(self))
      button.grid(row=5, column=1, sticky=tk.NSEW)

   # inverse button.
   def create_inverse_button(self):
      button = tk.Button(self.buttons_frame, text="1/x", bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: inverse(self))
      button.grid(row=1, column=1, sticky=tk.NSEW)

   # square button.
   def create_square_button(self):
      button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: square(self))
      button.grid(row=1, column=2, sticky=tk.NSEW)
   
   # sqrt button.
   def create_sqrt_button(self):
      button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: sqrt(self))
      button.grid(row=1, column=3, sticky=tk.NSEW)

   # clear button.
   def create_clear_button(self):
      button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: clear(self))
      button.grid(row=0, column=3, sticky=tk.NSEW)
      
      button = tk.Button(self.buttons_frame, text="CE", bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: clear(self))
      button.grid(row=0, column=2, sticky=tk.NSEW)

   # back button.
   def create_back_button(self):
      button = tk.Button(self.buttons_frame, text="\u2b05", bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: back(self))
      button.grid(row=0, column=4, sticky=tk.NSEW)

   # modulo button.
   def create_modulo_button(self):
      button = tk.Button(self.buttons_frame, text="%", bg=OFF_WHITE, fg=LABEL_COLOR,
                            font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: append_operator(self, '%'))
      button.grid(row=0, column=1, sticky=tk.NSEW)

   # Advanced Buttons.
   def create_dropdown_menus(self):
        frame = tk.Frame(self.window,  bg="#CCDEFF", height=10, width=20)
        frame.pack(expand=True, fill="both")
    
        options = ["cos", "sin", "tan", "sinh", "tanh", "cosh"]
        clicked = tk.StringVar()
        clicked.set("Trigo Functions")

        drop = tk.OptionMenu(frame, clicked, *options, command= lambda x : trigo(x ,self))
        drop.grid(row=0, column=0, columnspan=2)

        options = ["e^x", "e", "PI", "10^x"]
        clicked = tk.StringVar()
        clicked.set("Exponent Functions")

        drop = tk.OptionMenu(frame, clicked, *options, command=lambda x: log(x, self))
        drop.grid(row=0, column=2,columnspan=2)

   # Updating Labels.
   def update_total_label(self):
      expression = self.total_expression
      for operator, symbol in self.operators.items():
         expression = expression.replace(operator, f'{symbol}')
      self.total_label.config(text=expression)

   def update_label(self):
      self.current_expression = self.current_expression[:5]
      self.label.config(text=self.current_expression)

   # start calculating.
   def run(self):
      self.window.mainloop()

# Main Function.
if __name__ == "__main__":
   calc = Calculator()
   calc.run()