import tkinter

def recolor(widget, r, g, b):
	color = '#'
	for var in (r, g, b):
		color += 'FF' if var.get() else '00'
	widget.config(bg = color)
	
# Window.
window = tkinter.Tk()

# Frame
frame = tkinter.Frame(window)
frame.pack()

# Variables.
red = tkinter.IntVar()
green = tkinter.IntVar()
blue = tkinter.IntVar()

# Check Boxes.
for (name, var) in (('R', red), ('G', green), ('B', blue)):
	check = tkinter.Checkbutton(frame, text = name, variable = var)
	check.pack(side = 'left')
	
# Label And Button.
label = tkinter.Label(frame, text = '[		]')
button = tkinter.Button(frame, text = 'Update', command = lambda: recolor(label, red, green, blue))

button.pack(side = 'left')
label.pack(side = 'left')

window.mainloop()	