import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

# Label.
var = tkinter.StringVar()
label = tkinter.Label(frame, textvariable = var)
label.pack()

# Input.
entry = tkinter.Entry(frame, textvariable = var)
entry.pack()

window.mainloop()
