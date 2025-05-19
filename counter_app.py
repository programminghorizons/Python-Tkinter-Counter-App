import tkinter as tk

# Function to increment counter
def increment():
    try:
        outputLabel.config(text="")
        # Increment counter based on the entry value
        val = int(entry.get())
        val += 1
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(val))
    except ValueError:
        outputLabel.config(text="Invalid Input!")

# Function to decrement counter
def decrement():
    try:
        outputLabel.config(text="")
        # Decrement counter based on the entry value
        val = int(entry.get())
        val -= 1
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(val))
    except ValueError:
        outputLabel.config(text="Invalid Input!")


# Creating Main Window of the App
root = tk.Tk()
root.title('Counter App')
root.geometry('600x400')

# Place a label
inputLabel = tk.Label(root, text='Enter a Value', font=('Arial', 12))
inputLabel.pack()

# Place an entry widget
entry = tk.Entry(root, font=('verdana', 14), width=22)
entry.insert(tk.END, "0")  # Insert the default value as 0
entry.pack(pady=5)

# Create a small Frame to place two buttons side by side
buttonFrame = tk.Frame(root)
buttonFrame.pack()

# Place two button widgets
btnAdd = tk.Button(buttonFrame, text='Up', command=increment, font=('Arial', 12), bg="green", fg="white", width=10)
btnAdd.grid(row=0, column=0, padx=10, pady=5)

btnDown = tk.Button(buttonFrame, text='Down', command=decrement, font=('Arial', 12), bg="red", fg="white", width=10)
btnDown.grid(row=0, column=1, padx=10, pady=5)

# Place an output label to display result
outputLabel = tk.Label(root, text="", font=('Arial', 14))
outputLabel.pack()

root.mainloop()
