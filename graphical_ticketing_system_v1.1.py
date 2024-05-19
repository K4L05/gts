"""
Title:      Graphical Ticketing System
Author:     Kalos Robinson-Frani
Date:       16/05/24
Version:    1.1
Desc:       This program is a user interface for ordering tickets, and calculating the total price of selected tickets.
"""

# Importing libraries
from tkinter import *

class adult_tickets:
    def __init__(self) -> None:
        self.quantity = input_adult_ticket.get()
        self.cost = ticket_definitions["adult"]

    
    def calc_subtotal(self):
        return self.quantity * self.cost
    
    def tickets(self):
        return self.quantity

class child_tickets:
    def __init__(self) -> None:
        self.quantity = input_child_ticket.get()
        self.cost = ticket_definitions["child"]
    
    def calc_subtotal(self):
        return self.quantity * self.cost
    
    def tickets(self):
        return self.quantity
    

class stdsen_tickets:
    def __init__(self) -> None:
        self.quantity = input_stdsen_ticket.get()
        self.cost = ticket_definitions["student/senior"]
    
    def calc_subtotal(self):
        return self.quantity * self.cost
    
    def tickets(self):
        return self.quantity
    


ticket_definitions = {
    "adult": 15,
    "child": 5,
    "student/senior": 10
}

# GUI Setup
root = Tk()
root.title("GTS V1.0")

input_adult_ticket = IntVar()
input_child_ticket = IntVar()
input_stdsen_ticket = IntVar()

output_total_calc = IntVar()
output_total_calc.set("Total: $0")

def calculate():
    at = adult_tickets()
    ct = child_tickets()
    st = stdsen_tickets()

    total_tickets = at.tickets() + ct.tickets() + st.tickets()

    if total_tickets <= 100:
        total = (at.calc_subtotal() + ct.tickets() + st.calc_subtotal())
        output_total_calc.set(f"Total: ${total}")
    
    else:
        total = "Maximum # of tickets reached"
        output_total_calc.set(f"{total}")
    
    

Label(root, text="Adult     $15", width=20, font="Arial 30 bold").grid(row = 0, column=0)
Entry(root, textvariable=input_adult_ticket,width=20, justify="center", font="Arial 30 bold").grid(row=0, column=1)

Label(root, text="Child     $5", width=20, font="Arial 30 bold").grid(row = 1, column=0)
Entry(root, textvariable=input_child_ticket,width=20, justify="center", font="Arial 30 bold").grid(row=1, column=1)

Label(root, text="Student/Senior     $10", width=20, font="Arial 30 bold").grid(row = 2, column=0)
Entry(root, textvariable=input_stdsen_ticket,width=20, justify="center", font="Arial 30 bold").grid(row=2, column=1)
Label(root, textvariable=output_total_calc, font="Arial 20 bold").grid(row=3, column=0)
Button(root, text="Calculate", font="Arial 20 bold", command=calculate).grid(row=3, column=1)

# Run the UI
root.mainloop()
