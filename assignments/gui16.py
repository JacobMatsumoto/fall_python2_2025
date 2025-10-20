
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Initialize the main window
root = tk.Tk()
root.geometry("500x500")  # Set the window size
root.configure(bg="grey")  # Set the initial background color to white
root.title("test")

# I know we aren't supposed to use globals often, but I couldn't figure out how to get this done without one.
BACKGROUNDCOLORCYCLE = 1


def change_background():

    global BACKGROUNDCOLORCYCLE

    if BACKGROUNDCOLORCYCLE == 1:
        root.configure(bg="black")
        BACKGROUNDCOLORCYCLE = 2
    elif BACKGROUNDCOLORCYCLE == 2:
        root.configure(bg="brown")
        BACKGROUNDCOLORCYCLE = 3
    else:
        root.configure(bg="red")
        BACKGROUNDCOLORCYCLE = 1


poem = ["Roses are red", "Violets are blue",
        "Sugar is sweet", "and so are you"]
# I looked it up and you can do it like this https://labex.io/tutorials/python-how-to-retain-state-between-function-calls-420193


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        if self.count > 3:
            self.count = 0
        return self.count


poem_counter = Counter()


poems_label = tk.Label(root, text=poem[poem_counter.count], background="brown")
poems_label.pack(pady=10)


def update_poem_line():
    poem_counter.increment()
    current_index = poem_counter.count

    poems_label.config(text=poem[current_index])


poem_change = tk.Button(root, text="Next line", command=update_poem_line)
poem_change.pack(pady=10)
window_button = tk.Button(
    root, text="Change background", command=change_background)
window_button.pack(pady=10)


# https://www.geeksforgeeks.org/python/get-current-date-and-time-using-python/
def show_date_time():
    now = datetime.now()
    current_time = f"Year:{now.year} Month:{now.month} Day:{now.day} Hour:{now.hour} Minute:{now.minute}"
    messagebox.showinfo("Current Time", current_time)


date_time_button = tk.Button(root, text="Show time", command=show_date_time)
date_time_button.pack(pady=10)
# Start the Tkinter event loop
root.mainloop()
