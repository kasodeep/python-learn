import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(frame, text = "Registration Number")
label.pack(side = 'left')

entry = tkinter.Entry(frame)
entry.pack(side = 'left')

window.mainloop()