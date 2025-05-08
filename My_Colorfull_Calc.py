from tkinter import *
import math

# Function to update the input field
def btn_click(value):
    current = text_Input.get()
    text_Input.set(current + str(value))

# Function to clear the input field
def btn_clear():
    text_Input.set("")

# Function to evaluate the expression
def btn_equal():
    try:
        result = eval(text_Input.get())
        text_Input.set(result)
    except Exception as e:
        text_Input.set("Error")

# Function to delete the last character
def btn_delete():
    current = text_Input.get()
    text_Input.set(current[:-1])

# Function for factorial
def factorial():
    try:
        value = int(text_Input.get())
        if value < 0:
            text_Input.set("Error")
        else:
            result = math.factorial(value)
            text_Input.set(result)
    except ValueError:
        text_Input.set("Error")

# Function to toggle the sign of the number
def toggle_sign():
    current = text_Input.get()
    if current:
        if current[0] == "-":
            text_Input.set(current[1:])
        else:
            text_Input.set("-" + current)

# Function to calculate square root
def square_root():
    try:
        value = float(text_Input.get())
        result = math.sqrt(value)
        text_Input.set(result)
    except ValueError:
        text_Input.set("Error")

# Function to calculate the logarithm (natural log)
def log():
    try:
        value = float(text_Input.get())
        result = math.log(value)
        text_Input.set(result)
    except ValueError:
        text_Input.set("Error")

# Function to calculate sine
def sin_func():
    try:
        value = float(text_Input.get())
        result = math.sin(math.radians(value))
        text_Input.set(result)
    except ValueError:
        text_Input.set("Error")

# Function to calculate cosine
def cos_func():
    try:
        value = float(text_Input.get())
        result = math.cos(math.radians(value))
        text_Input.set(result)
    except ValueError:
        text_Input.set("Error")

# Function to calculate tangent
def tan_func():
    try:
        value = float(text_Input.get())
        result = math.tan(math.radians(value))
        text_Input.set(result)
    except ValueError:
        text_Input.set("Error")

# Function for exponentiation
def exponent():
    try:
        value = float(text_Input.get())
        result = math.exp(value)
        text_Input.set(result)
    except ValueError:
        text_Input.set("Error")

# Initialize the main window
cal = Tk()
cal.title("Calculator")
text_Input = StringVar()
cal.resizable(width=True, height=True)

# Entry field
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=5,
                   insertwidth=6, bg="coral", justify='right')
txtDisplay.grid(columnspan=9)

# Define the buttons with their colors
buttons = [
    ('1', 1, 0, "lightgreen"), ('2', 1, 1, "lightpink"), ('3', 1, 2, "cyan"), ('+', 1, 3, "orange"),
    ('4', 2, 0, "lightgreen"), ('5', 2, 1, "lightpink"), ('6', 2, 2, "cyan"), ('-', 2, 3, "orange"),
    ('7', 3, 0, "lightgreen"), ('8', 3, 1, "lightpink"), ('9', 3, 2, "cyan"), ('*', 3, 3, "orange"),
    ('0', 5, 0, "lightgreen"), ('%', 4, 3, "orange"), ('/', 5, 2, "cyan"), ('n!', 5, 3, "orange"),
    ('+/-', 4, 0, "lightgreen"), ('sin', 4, 1, "lightpink"), ('cos', 4, 2, "cyan"), ('tan', 5, 1, "lightpink"),
    ('<-', 6, 0, "lightgreen"), ('Ln', 6, 1, "lightpink"), ('√', 6, 2, "cyan"), ('C', 6, 3, "orange"),
    ('Exp', 7, 0, "orange"), ('x^2', 7, 1, "orange"), ('=', 7, 2, "orange")
]

# Add the buttons to the window with corresponding colors
for (text, row, col, color) in buttons:
    if text == '=':
        button = Button(cal, padx=16, bd=8, fg="black", font=('calibri', 24, 'bold'),
                        text=text, bg=color, command=btn_equal)
        button.grid(row=row, column=col, columnspan=2, sticky="nsew")  # Expand "=" button over two columns
    elif text == 'C':
        button = Button(cal, padx=16, bd=8, fg="black", font=('aerial', 20, 'bold'),
                        text=text, bg=color, command=btn_clear)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == '<-':
        button = Button(cal, padx=16, bd=8, fg="black", font=('aerial', 20, 'bold'),
                        text=text, bg="lightgreen", command=btn_delete)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == 'n!':
        button = Button(cal, padx=16, bd=8, fg="black", font=('aerial', 20, 'bold'),
                        text=text, bg=color, command=factorial)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == 'sin':
        button = Button(cal, padx=16, bd=8, fg="black", font=('calibri', 20, 'bold'),
                        text=text, bg="lightpink", command=sin_func)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == 'cos':
        button = Button(cal, padx=16, bd=8, fg="black", font=('calibri', 20, 'bold'),
                        text=text, bg="cyan", command=cos_func)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == 'tan':
        button = Button(cal, padx=16, bd=8, fg="black", font=('calibri', 20, 'bold'),
                        text=text, bg="lightpink", command=tan_func)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == 'Ln':
        button = Button(cal, padx=16, bd=8, fg="black", font=('aerial', 20, 'bold'),
                        text=text, bg="lightpink", command=log)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == '√':
        button = Button(cal, padx=16, bd=8, fg="black", font=('aerial', 22, 'bold'),
                        text=text, bg="cyan", command=square_root)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == 'Exp':
        button = Button(cal, padx=16, bd=8, fg="black", font=('calibri', 20, 'bold'),
                        text=text, bg="orange", command=exponent)
        button.grid(row=row, column=col, sticky="nsew")
    elif text == '+/-':
        button = Button(cal, padx=16, bd=8, fg="black", font=('aerial', 20, 'bold'),
                        text=text, bg="lightgreen", command=toggle_sign)
        button.grid(row=row, column=col, sticky="nsew")
    else:
        button = Button(cal, padx=16, bd=8, fg="black", font=('aerial', 20, 'bold'),
                        text=text, bg=color, command=lambda t=text: btn_click(t))
        button.grid(row=row, column=col, sticky="nsew")

# Start the Tkinter main loop
cal.mainloop()
