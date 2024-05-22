"""
Title:      Graphical Ticketing System
Author:     Kalos Robinson-Frani
Date:       21/05/24
Version:    2.0
Desc:       This program is a user interface for ordering tickets, and calculating the total price of selected tickets.
"""

# Importing libraries
from tkinter import *

ticket_definitions = {
    "adult": 15,
    "child": 5,
    "student/senior": 10
}

class ticket:
    def __init__(self) -> None:
        pass

    class adult:
        def __init__(self) -> None:
            self.quantity = input_adult_ticket.get()
            self.cost = ticket_definitions["adult"]

        
        def calc_subtotal(self):
            return self.quantity * float(self.cost)
        
        def tickets(self):
            return self.quantity

    class child:
        def __init__(self) -> None:
            self.quantity = input_child_ticket.get()
            self.cost = ticket_definitions["child"]
        
        def calc_subtotal(self):
            return self.quantity * float(self.cost)
        
        def tickets(self):
            return self.quantity
        

    class stdsen:
        def __init__(self) -> None:
            self.quantity = int(input_stdsen_ticket.get())
            self.cost = ticket_definitions["student/senior"]
        
        def calc_subtotal(self):
            return self.quantity * float(self.cost)
        
        def tickets(self):
            return self.quantity
    


# GUI Setup
root = Tk()
root.title("GTS V2.0")

input_adult_ticket = IntVar()
input_child_ticket = IntVar()
input_stdsen_ticket = IntVar()

output_total_calc = IntVar()
output_total_calc.set("Total: $0")

def calculate():
    at = ticket().adult()
    ct = ticket().child()
    st = ticket().stdsen()
    total_tickets = at.tickets() + ct.tickets() + st.tickets()

    if total_tickets <= 100:
        total = (at.calc_subtotal() + ct.tickets() + st.calc_subtotal())
        output_total_calc.set(f"Total: ${total}")
    
    else:
        total = "Maximum # of tickets reached"
        output_total_calc.set(f"{total}")
    
    
Label(root, text="Graphical Ticketing System", justify="center", font="Arial 30 bold").grid(row = 0, column=0, columnspan=3)

Mainframe = Frame(root).grid(row=1, column=0, columnspan=2)
Label(Mainframe, text="type", width=15, font="Arial 24 bold").grid(row=1, column=0)
Label(Mainframe, text="price", width=15, font="Arial 24 bold").grid(row=1, column=1)
Label(Mainframe, text="order", width=15, font="Arial 24 bold").grid(row=1, column=2)

Subframe = Frame(Mainframe).grid(row=0, column=0, columnspan=3)

Label(Subframe, text="Adult", font="Arial 18", width=15).grid(row = 2, column=0)
Label(Subframe, text="$15", font="Arial 18", width=15).grid(row=2, column=1)
Entry(Subframe, width="15", textvariable=input_adult_ticket, justify="center", font="Arial 30 bold").grid(row=2, column=2)

Label(Subframe, text="Child", font="Arial 18", width=15).grid(row = 3, column=0)
Label(Subframe, text="$5", font="Arial 18", width=15).grid(row=3, column=1)
Entry(Subframe, width="15", textvariable=input_child_ticket, justify="center", font="Arial 30 bold").grid(row=3, column=2)


Label(Subframe, text="Student/Senior", font="Arial 18", width=15).grid(row = 4, column=0)
Label(Subframe, text="$10", font="Arial 18", width=15).grid(row=4, column=1)
Entry(Subframe, width="15", textvariable=input_stdsen_ticket, justify="center", font="Arial 30 bold").grid(row=4, column=2)

Label(Mainframe, textvariable=output_total_calc, font="Arial 20 bold").grid(row=5, column=0, columnspan=2)
Button(Mainframe, text="Calculate", font="Arial 20 bold", command=calculate).grid(row=5, column=2)

# Run the UI
root.mainloop()
