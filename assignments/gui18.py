
import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x400")  # Set the window size
root.configure(bg="grey")  # Set the initial background color to white

# Function to change the background color to black


def change_color():
    root.configure(bg="purple")


def change_color_back():
    root.configure(bg="grey")
# Schedule the change_color function to be called after 1000 milliseconds (1 seconds)

root.after(1000, change_color)

root.after(2000, change_color_back)
 

# Add a button that says "Goodbye!"
goodbye_button = tk.Button(root, text="Goodbye!", command=root.destroy)
goodbye_button.pack(pady=20)

change_goodbye = tk.Button(root, text="Change Goodbye!",
                           command=lambda: goodbye_button.config(text="See ya!"))
change_goodbye.pack(pady=10)

window_button = tk.Button(root, text="Change window size",
                           command=lambda: root.geometry("500x700"))
window_button.pack(pady=10)
# Set focus on the goodbye button
goodbye_button.focus_set()

# Start the Tkinter event loop
root.mainloop()
