import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    operation = operation_var.get()

    try:
        if operation == "Square Root":
            num = float(entry1.get())
            if num < 0:
                result_label.config(text="Cannot find square root of a negative number")
            else:
                result_label.config(text=f"Result: {round(math.sqrt(num), 2)}")
            return

        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2

        elif operation == "Percentage":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = (num1 / num2) * 100

        elif operation == "Power":
            result = num1 ** num2

        elif operation == "Modulus":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 % num2

        result_label.config(text=f"Result: {round(result,2)}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x350")

tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

operation_var = tk.StringVar()
operation_var.set("Addition")

operations = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Percentage",
    "Power",
    "Square Root",
    "Modulus"
]

tk.OptionMenu(root, operation_var, *operations).pack(pady=10)

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="Result:", font=("Arial", 12))
result_label.pack()

root.mainloop()
