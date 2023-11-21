import tkinter
import tkinter.filedialog as dialog

# Function to save the file.
def save(root,text):

	data = text.get('0.0', tkinter.END)
	filename = dialog.asksaveasfilename(parent = root, filetypes = [('Text', '*.txt')], title = 'Save as...')
	
	writer = open(filename, 'w')
	writer.write(data)
	writer.close()
	
# Quit Function.
def quit(root):
	root.destroy()
	
# Window.
window = tkinter.Tk()

# Text.
text = tkinter.Text(window)
text.pack()

# Menubar.
menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar)

# Options.
filemenu.add_command(label = 'Save', command = lambda:save(window,text))
filemenu.add_command(label = 'Quit', command = lambda:quit(window))

# File
menubar.add_cascade(label = 'File', menu = filemenu)
window.config(menu = menubar)

window.mainloop()

