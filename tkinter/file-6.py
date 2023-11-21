import tkinter

def increment():
	counter.set(counter.get() + 1)
	
def decrement():
	counter.set(counter.get() - 1)
	
if __name__ == '__main__':
	window = tkinter.Tk()
	
	# Model
	counter = tkinter.IntVar()
	counter.set(0)
		
	# Views 
	frame = tkinter.Frame(window)
	frame.pack()
	
	button = tkinter.Button(frame, text = 'Increment', command = increment)
	button.pack()		
	
	button = tkinter.Button(frame, text = 'Decrement', command = decrement)
	button.pack()
	
	label = tkinter.Label(frame, textvariable = counter)
	label.pack()
		
	# Start the machinery
	window.mainloop()