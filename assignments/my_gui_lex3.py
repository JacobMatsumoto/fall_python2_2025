import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Coffee Shop Menu")
root.geometry("500x500")

# Step 1: Create the Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Variables to store order details and prices now too
num_coffees = tk.IntVar(value=0)
coffee_price = 2
num_cream = tk.IntVar(value=0)
num_sugar = tk.IntVar(value=0)
num_teas = tk.IntVar(value=0)
tea_price = 2
num_lemon = tk.IntVar(value=0)
num_honey = tk.IntVar(value=0)
# Donuts + prices
num_pf_donuts = tk.IntVar(value=0)
pf_d_price = 1
num_bc_donuts = tk.IntVar(value=0)
bc_d_price = 1.75
num_dblchoc_donuts = tk.IntVar(value=0)
dblchoc_d_price = 1.50
num_lj_donuts = tk.IntVar(value=0)
lj_d_price = 2
num_bb_donuts = tk.IntVar(value=0)
bb_d_price = 1
# bagels + prices
num_p_bagels = tk.IntVar(value=0)
pb_price = 1
num_e_bagels = tk.IntVar(value=0)
eb_price = 1.50
num_a_bagels = tk.IntVar(value=0)
ab_price = 2.25
num_tc_bagels = tk.IntVar(value=0)
tcb_price = 2
num_bb_bagels = tk.IntVar(value=0)
bbb_price = 1.75
# Step 2: Create Menus


def show_drinks():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    drinks_frame = tk.Frame(root)
    drinks_frame.pack(padx=10, pady=10)

    tk.Label(drinks_frame, text="Number of Coffees:").grid(
        row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_coffees, *range(11)
                  ).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Cream:").grid(
        row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_cream, *range(11)
                  ).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Sugar:").grid(
        row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_sugar, *range(11)
                  ).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Teas:").grid(
        row=3, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_teas, *range(11)
                  ).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Lemon:").grid(
        row=4, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_lemon, *range(11)
                  ).grid(row=4, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Honey:").grid(
        row=5, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_honey, *range(11)
                  ).grid(row=5, column=1, padx=10, pady=5)


def show_donuts():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    donuts_frame = tk.Frame(root)
    donuts_frame.pack(padx=10, pady=10)
    # Students will complete this section
    tk.Label(donuts_frame, text="Number of Pink Frosted Donuts:").grid(
        row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame, num_pf_donuts, *range(11)
                  ).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(donuts_frame, text="Number of Boston Cream Donuts:").grid(
        row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame, num_bc_donuts, *range(11)
                  ).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(donuts_frame, text="Number of Double Chocolate Donuts:").grid(
        row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame, num_dblchoc_donuts, *range(11)
                  ).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(donuts_frame, text="Number of Long John Donuts:").grid(
        row=3, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame, num_lj_donuts, *range(11)
                  ).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(donuts_frame, text="Number of Blueberry Donuts:").grid(
        row=4, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame, num_bb_donuts, *range(11)
                  ).grid(row=4, column=1, padx=10, pady=5)


def show_bagels():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    bagels_frame = tk.Frame(root)
    bagels_frame.pack(padx=10, pady=10)
    # Students will complete this section
    tk.Label(bagels_frame, text="Number of Plain Bagels:").grid(
        row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_p_bagels, *range(11)
                  ).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(bagels_frame, text="Number of Everything Bagels:").grid(
        row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_e_bagels, *range(11)
                  ).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(bagels_frame, text="Number of Asiago Bagels:").grid(
        row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_a_bagels, *range(11)
                  ).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(bagels_frame, text="Number of Three Cheese Bagels:").grid(
        row=3, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_tc_bagels, *range(11)
                  ).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(bagels_frame, text="Number of Blueberry Bagels:").grid(
        row=4, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_bb_bagels, *range(11)
                  ).grid(row=4, column=1, padx=10, pady=5)


# Create Menus and add to Menu Bar
drinks_menu = tk.Menu(menu_bar, tearoff=0)
donuts_menu = tk.Menu(menu_bar, tearoff=0)
bagels_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Drinks", menu=drinks_menu)
menu_bar.add_cascade(label="Donuts", menu=donuts_menu)
menu_bar.add_cascade(label="Bagels", menu=bagels_menu)

# Add menu items and assign commands to the menus
drinks_menu.add_command(label="Show Drinks", command=show_drinks)
donuts_menu.add_command(label="Show Donuts", command=show_donuts)
bagels_menu.add_command(label="Show Bagels", command=show_bagels)

# Function to display the order summary


def show_order():

    # Donut totals
    pf_donut_total = num_pf_donuts.get() * pf_d_price
    bc_donut_total = num_bc_donuts.get() * bc_d_price
    dblchoc_donut_total = num_dblchoc_donuts.get() * dblchoc_d_price
    lj_donut_total = num_lj_donuts.get() * lj_d_price
    bb_donut_total = num_bb_donuts.get() * bb_d_price

    # Bagel totals
    p_bagel_total = num_p_bagels.get() * pb_price
    e_bagel_total = num_e_bagels.get() * eb_price
    a_bagel_total = num_a_bagels.get() * ab_price
    tc_bagel_total = num_tc_bagels.get() * tcb_price
    bb_bagel_total = num_bb_bagels.get() * bbb_price

    # Total prices
    coffee_total = num_coffees.get() * coffee_price

    tea_total = num_teas.get() * tea_price

    donut_total_price = pf_donut_total + bc_donut_total + \
        dblchoc_donut_total + lj_donut_total + bb_donut_total

    bagel_total_price = p_bagel_total + e_bagel_total + \
        a_bagel_total + tc_bagel_total + bb_bagel_total

    # I didn't like how multiplication was being done in total cost, readability for me at least was bad.
    # So i did the multiplication all before going to total. I also added prices for coffee and tea because I didn't like the price not being represented by a variable.
    total_cost = coffee_total + tea_total + bagel_total_price + donut_total_price

    order = (f"Coffees: {num_coffees.get()}, Cream: {num_cream.get()}, Sugar: {num_sugar.get()}\n"
             f"Teas: {num_teas.get()}, Lemon: {num_lemon.get()}, Honey: {num_honey.get()}\n"
             f"Donuts: Pink Frosted: {num_pf_donuts.get()}, Boston Cream: {num_bc_donuts.get()},\nDouble Chocolate: {num_dblchoc_donuts.get()}, Long John: {num_lj_donuts.get()}, Blueberry: {num_bb_donuts.get()}\n"
             f"Bagels: Plain: {num_p_bagels.get()}, Everything: {num_e_bagels.get()}, Asiago: {num_a_bagels.get()},\nThree Cheese: {num_tc_bagels.get()}, Blueberry: {num_bb_bagels.get()}\n"
             f"Total Cost: ${total_cost}")
    messagebox.showinfo("Order Summary", order)


# Create a Button to complete the order
complete_order_button = tk.Button(
    root, text="Complete Order", command=show_order)
complete_order_button.pack(pady=10)

# Run the application
root.mainloop()
