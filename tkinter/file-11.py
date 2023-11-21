import tkinter

def cross(text):
	text.insert(tkinter.INSERT, '*')
	
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

# Height And Width.
text = tkinter.Text(frame, height = 10, width = 30)
text.pack()

button = tkinter.Button(frame, text = "Add", command = lambda: cross(text))
button.pack()

window.mainloop()