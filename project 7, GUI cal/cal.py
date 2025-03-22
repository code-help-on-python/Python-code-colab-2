import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x500")

        self.entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sqrt', 5, 0), ('**', 5, 1), ('log', 5, 2), ('C', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('Exit', 6, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=2, font=("Arial", 12),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == "C":
            self.entry.delete(0, tk.END)
        elif value == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
        elif value == "sqrt":
            try:
                num = float(self.entry.get())
                result = math.sqrt(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif value == "log":
            try:
                num = float(self.entry.get())
                result = math.log(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif value in ["sin", "cos", "tan"]:
            try:
                num = float(self.entry.get())
                if value == "sin":
                    result = math.sin(math.radians(num))
                elif value == "cos":
                    result = math.cos(math.radians(num))
                else:
                    result = math.tan(math.radians(num))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif value == "Exit":
            self.root.quit()
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
    