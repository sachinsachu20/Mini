import tkinter as tk

def calculate(expression):
    try:
        result = eval(expression)
        return f"{expression} = {result}"
    except Exception as e:
        return "Error"

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def equals():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, calculate(current))

# Create the main window
root = tk.Tk()
root.title("Calculator")  # Set a title for the window

# Create an Entry widget
entry = tk.Entry(root, font=('Arial', 24), width=16)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons with increased size
buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    'C', '0', '=', '/'
]

for i, button in enumerate(buttons):
    if button == '=':
        btn = tk.Button(root, text=button, command=equals, width=5, height=2, font=('Arial', 18))
    elif button == 'C':
        btn = tk.Button(root, text=button, command=clear, width=5, height=2, font=('Arial', 18))
    else:
        btn = tk.Button(root, text=button, command=lambda b=button: button_click(b), width=5, height=2, font=('Arial', 18))
    
    btn.grid(row=(i // 4) + 1, column=i % 4)

# Start the Tkinter main loop
root.mainloop()
