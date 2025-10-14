import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("color changing button")


root.config(bg='#D3D3D3')


def color1():
    """
    creates a button with a command that destroys and recreates with different colors using the other function. 
    """
    global change_button
    change_button = tk.Button(
        root,
        text="Color!",
        bg='#4CAF50',
        fg='#FFFFFF',
        # Here I passed the command a lamda containing 2 functions, one is tkinters destroy and the other is the color2 function I made
        command=lambda: (change_button.destroy(), color2())
    )
    change_button.grid(
        row=0,
        padx=5,
        pady=5,
        column=0
    )


def color2():
    """
    recreates the button made with new colors and can be pressed to delete itself and recreate the first button
    """
    global change_button
    change_button = tk.Button(
        root,
        text="New Color!",
        bg="#E60000",
        fg="#000000",
        # Here I passed the command a lamda containing 2 functions, one is tkinters destroy and the other is the color1 function I made
        command=lambda: (change_button.destroy(), color1())
    )
    change_button.grid(
        row=0,
        padx=5,
        pady=5,
        column=0
    )


def reset_color():
    """
    resets button to the original state
    """
    change_button = tk.Button(
        root,
        text="Color!",
        bg='#4CAF50',
        fg='#FFFFFF',
        command=color1)
    change_button.grid(row=0, padx=5, pady=5, column=0)


# Destroys current button and replaces it with the original.
reset_button = tk.Button(
    root,
    text="Reset",
    bg="#000000",
    fg="#FFFB04",
    # Here I passed the command a lamda containing 2 functions, one is tkinters destroy and the other is the reset color function I made
    command=lambda: (change_button.destroy(), reset_color())
)
reset_button.grid(row=1, padx=5, pady=5, column=1)

color1()

# Run the Tkinter event loop
root.mainloop()
# I had a few issues figuring out how to get two functions into a command because I needed to destroy the button AND make it change color. I missed config in the readings for changing aspects of buttons and ended up over working on this assignment.
