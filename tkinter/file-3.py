import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

frame2 = tkinter.Frame(window, borderwidth = 10, relief = tkinter.GROOVE)
frame2.pack()

window.mainloop()