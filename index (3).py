import tkinter as tk

# Function to update the display
def button_click(value):
    current = display_var.get()
    display_var.set(current + value)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception:
        display_var.set("Error")

# Function to clear the display
def clear():
    display_var.set("")

# Main window setup
root = tk.Tk()
root.title("Calculator")

# Variable to store display text
display_var = tk.StringVar()

# Display screen
display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 18), bd=10, insertwidth=2, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create buttons in a loop
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                  command=calculate).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, sticky="nsew")

# Clear button
tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18),
          command=clear).grid(row=5, column=0, columnspan=4, sticky="nsew")

# Configure rows and columns to adjust with window size
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the GUI
root.mainloop()
