import tkinter

# MVC Architecture.

# Controller
def click():
   counter.set(counter.get() + 1)

if __name__ == '__main__':
   window = tkinter.Tk()

   # Model
   counter = tkinter.IntVar()
   counter.set(0)

   # Views
   frame = tkinter.Frame(window)
   frame.pack()

   button = tkinter.Button(frame, text = 'Click', command = click)
   button.pack()

   label = tkinter.Label(frame, textvariable = counter)
   label.pack()

   # Start the Machine
   window.mainloop()