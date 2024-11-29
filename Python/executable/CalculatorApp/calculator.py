import tkinter as tk
from tkinter import messagebox

# Create the main window
app = tk.Tk()
app.title("Calculator")
app.geometry("300x400")

# Entry field for displaying input and output
entry = tk.Entry(app, width=20, font=("Arial", 24), bd=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function for button click
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the input
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(app, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    elif text == "C":
        tk.Button(app, text=text, width=5, height=2, command=clear).grid(row=row, column=col)
    else:
        tk.Button(app, text=text, width=5, height=2, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Run the application
app.mainloop()
