from tkinter import *
from tkinter import ttk
import random
from SortingAlgos import *
from tkinter import messagebox

HEIGHT = 500
WIDTH = 700

root = Tk()
root.title('Sorting Visualized!')

# Variables 
selected_algo = StringVar()
data = []
exitFlag = False

# Functions
def drawData(data, colorArray):
	mainFrame.delete('all')
	c_height = mainFrame.winfo_height() - 10
	c_width = mainFrame.winfo_width()
	x_width = c_width / (len(data) + 1)
	offset = (c_width)/(len(data)*10)
	spacing = 10

	for i, height in enumerate(data):
		# Top Left
		x0 = i * x_width + offset + spacing
		y0 = c_height - height*(c_height-30)

		# Bottom Right
		x1 = (i + 1) * x_width + offset
		y1 = c_height

		mainFrame.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
	root.update()

def generate():
	global data

	# minVal = int(minEntry.get())
	# maxVal = int(maxEntry.get())
	size = int(sizeEntry.get())

	data = [i for i in range(1,size)]
	# data = [random.randint(minVal, maxVal) for i in range(1,size)] # For generating data in given range
	random.shuffle(data)

	# Normalizing data
	data = [i/max(data) for i in data]

	drawData(data, ['#3b4249' for _ in range(len(data))])

def startAlgorithm():
	global data

	if data == sorted(data):
		return
		
	# Disabling Once ALgo is Started
	startB['state'] = 'disabled'	
	genB['state'] = 'disabled'

	algorithm = ('_').join(algMenu.get().lower().split())
	eval(algorithm + '(data, drawData, speedScale.get())')
        
	# Enabling the Button again
	startB['state'] = 'normal'	
	genB['state'] = 'normal'

# Main Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

UI_Frame = Frame(root, width=WIDTH, height=HEIGHT, bg='black', bd=10)
UI_Frame.place(relx=0.5, rely=0, relwidth=0.96, relheight=0.3, anchor='n')

# Menu Row [1]
Label(UI_Frame, text='Algorithm', bg="grey", font=('Courier', 20, "italic bold"),relief=GROOVE,fg="black", bd=5, width=10).place(x=0, y=0)
#font=("new roman", 16, "italic bold"), bg="#05897A",
                  #width=10, fg="black", relief=GROOVE, bd=5)
				 


# Algorithm Selection Dropdown
algMenu = ttk.Combobox(UI_Frame, textvariable=selected_algo, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort'], font=('Courier', 15))
algMenu.place(x=50, y=35, relheight=0.2, relwidth=0.4)
algMenu.current(0)

speedScale = Scale(UI_Frame, from_=0.2, to=0.0, length=200, digits=2, resolution=0.0, orient=HORIZONTAL, label='Select Speed [sec]',bg="gray", font=('Courier', 20, "italic bold"),relief=GROOVE,fg="black", bd=5, width=10)
speedScale.place(relx=0.5, rely=0, relheight=0.47, relwidth=0.35)

# Start Button
startB = Button(UI_Frame, text="Start", command=startAlgorithm, bg='gray', font=('Courier', 20, "italic bold"),relief=GROOVE,fg="black", bd=5, width=10)
startB.place(relx=0.87, rely=0.1, relwidth=0.13, relheight=0.3)

# Menu Row[2] (Entry Scales)
sizeEntry = Scale(UI_Frame, from_=10, to=150, resolution=1, orient=HORIZONTAL, label='Data Size',bg="gray" , font=('Courier', 20, "italic bold"),relief=GROOVE,fg="black", bd=5, width=10)
#font=('Courier', 12)
sizeEntry.place(relx=0, rely=0.53, relheight=0.47, relwidth=0.25)

minEntry = Scale(UI_Frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label='Min Value',bg="gray",font=('Courier', 20, "italic bold"),relief=GROOVE,fg="black", bd=5, width=10)
minEntry.place(relx=0.30, rely=0.53, relheight=0.47, relwidth=0.25)

maxEntry = Scale(UI_Frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Max Value',bg="gray", font=('Courier', 20, "italic bold"),relief=GROOVE,fg="black", bd=5, width=10)
maxEntry.place(relx=0.6, rely=0.53, relheight=0.47, relwidth=0.25)

# Generate Button
genB = Button(UI_Frame, text="Generate", command=generate, bg='gray', fg='white', font=('Courier', 20, "italic bold"),relief=GROOVE,  bd=5, width=10)
genB.place(relx=0.87, rely=0.6, relwidth=0.13, relheight=0.3)

mainFrame = Canvas(root, bg='black')
mainFrame.place(relx=0.5, rely=0.31, relwidth=0.98, relheight=0.68, anchor='n')

def on_closing():
	global exitFlag
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

