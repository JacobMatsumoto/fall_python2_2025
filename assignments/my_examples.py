# Importing necessary modules
import tkinter as tk
from tkinter import messagebox

# Function to be called when the button is clicked


def on_button_click():
    # Print message to the console
    print("Hello")
    # Show message box with the message
    messagebox.showinfo("Message", "Hello")

# Function to quit the application


def on_quit():
    window.destroy()


# Create the main window
window = tk.Tk()
window.title("Simple GUI Application")

# Create a button and set its command property
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Create a quit button and set its command property
quit_button = tk.Button(window, text="Quit", command=on_quit)
quit_button.pack(pady=10)

# Run the application
window.mainloop()
