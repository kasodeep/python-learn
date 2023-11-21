import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

# GRID
label = tkinter.Label(frame, text = 'Name')
label.grid(row = 0, column = 0)

entry = tkinter.Entry(frame)
entry.grid(row = 0, column = 1)

label = tkinter.Label(frame, text = 'Reg. No.')
label.grid(row = 1, column = 0)

entry = tkinter.Entry(frame)
entry.grid(row = 1, column = 1)

label = tkinter.Label(frame, text = 'Mob. No.')
label.grid(row = 2, column = 0)

entry = tkinter.Entry(frame)
entry.grid(row = 2, column = 1)

window.mainloop()