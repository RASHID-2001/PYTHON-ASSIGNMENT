"""

QN:Write a GUI-based program that allows the user to convert amount in Indian
Rupees to amount in Euro.
The interface should have labeled entry fields for these two values. These
components should be arranged in a grid where the labels occupy the first row
and the corresponding fields occupy the second row.
At start-up, the Rupees field should contain 0.0, and the Euro field should contain
0.0. The third row in the window contains two command buttons, labeled R->E
and E->R. When the user presses the first button, the program should use the data
in the Rupee field to compute the amount in Euro, which should then be output
to the Euro field. The second button should perform the inverse function.(MAY2023)

"""

from tkinter import *


RUPEE_TO_EURO = 0.011  
EURO_TO_RUPEE = 1 / RUPEE_TO_EURO  # 1 EUR = 90.91 INR (approx)

def rupees_to_euro():
    try:
        rupees = float(rupee_entry.get())
        euros = rupees * RUPEE_TO_EURO
        euro_entry.delete(0, END)
        euro_entry.insert(0, f"{euros:.2f}")  # Display formatted value
    except ValueError:
        euro_entry.delete(0, END)
        euro_entry.insert(0, "Invalid input")

def euro_to_rupees():
    try:
        euros = float(euro_entry.get())
        rupees = euros * EURO_TO_RUPEE
        rupee_entry.delete(0, END)
        rupee_entry.insert(0, f"{rupees:.2f}")
    except ValueError:
        rupee_entry.delete(0, END)
        rupee_entry.insert(0, "Invalid input")


root = Tk()
root.title("Currency Converter")
root.geometry("300x150")
root.resizable(False, False)


Label(root, text="Indian Rupees (INR)").grid(row=0, column=0, padx=10, pady=5)
Label(root, text="Euros (EUR)").grid(row=0, column=1, padx=10, pady=5)

rupee_entry = Entry(root)
rupee_entry.grid(row=1, column=0, padx=10, pady=5)
rupee_entry.insert(0, "0.0")  # Default value

euro_entry = Entry(root)
euro_entry.grid(row=1, column=1, padx=10, pady=5)
euro_entry.insert(0, "0.0")  # Default value


Button(root, text="R → E", command=rupees_to_euro).grid(row=2, column=0, padx=10, pady=10)
Button(root, text="E → R", command=euro_to_rupees).grid(row=2, column=1, padx=10, pady=10)


root.mainloop()
