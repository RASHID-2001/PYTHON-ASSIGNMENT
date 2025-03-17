"""
QN:Design a Python GUI program that takes user input for the length and width of a
rectangle, and when a button is pressed, calculates and displays the area of the
rectangle.(MAY 2024)

"""
from tkinter import *

def calculate_area():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = length * width
        result_label.config(text=f"Area: {area:.2f} square units")
    except ValueError:
        result_label.config(text="Invalid input! Enter numbers.")


root = Tk()
root.title("Rectangle Area Calculator")
root.geometry("300x200")
root.resizable(False, False)


Label(root, text="Enter Length:").pack(pady=5)
length_entry = Entry(root)
length_entry.pack(pady=5)

Label(root, text="Enter Width:").pack(pady=5)
width_entry = Entry(root)
width_entry.pack(pady=5)


Button(root, text="Calculate Area", command=calculate_area).pack(pady=10)


result_label = Label(root, text="")
result_label.pack(pady=10)


root.mainloop()
