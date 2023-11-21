import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

a = tkinter.Label(frame, text = "One")
a.pack()

b = tkinter.Label(frame, text = "Two")
b.pack()

c = tkinter.Label(frame, text = "Three")
c.pack()

window.mainloop()
