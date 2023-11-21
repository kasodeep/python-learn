import tkinter

# Window Object.
window = tkinter.Tk()

# Data.
data = tkinter.StringVar()
data.set('Kasodariya Deep')

# Label on Window.
label = tkinter.Label(window, textvariable = data)
label.pack()

help(window.mainloop)
window.mainloop()