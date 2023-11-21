import tkinter

# Controller
def click(var, value):
	var.set(var.get() + value)

if __name__ == '__main__':
	window = tkinter.Tk()
	
	# Model
	counter = tkinter.IntVar()
	counter.set(0)
	
	# Views 
	frame = tkinter.Frame(window)
	frame.pack()
	
	button = tkinter.Button(frame, text = 'Increment', command = lambda: click(counter, 1))
	button.pack()		
	
	button = tkinter.Button(frame, text = 'Decrement', command = lambda: click(counter, -1))
	button.pack()
	
	label = tkinter.Label(frame, textvariable = counter)
	label.pack()
		
	# Start the machinery
	window.mainloop()