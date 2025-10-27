# Import necessary modules
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.geometry("300x300")
root.title("Goal Setter")

# Create a static text label

# Create a dynamic text label using a textvariable
dynamic_text = tk.StringVar()
dynamic_text.set("Lets set goals for today!")
dynamic_label = tk.Label(root, textvariable=dynamic_text)
dynamic_label.pack()

# Message https://www.geeksforgeeks.org/python/python-tkinter-message/ Text was displaying funny, it was because no width was set. This page gave me each thing I can change.
message = tk.Message(
    root, text="Enter your goals for today in the entry fields bellow.", width="275")
message.pack()

#Frame
row1 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
row1.pack(padx=10, pady=10)
row2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
row2.pack(padx=10, pady=10)

# Add labels to the frame
# https://www.geeksforgeeks.org/python/python-pack-method-in-tkinter/ use of LEFT outdated, but works similarly, it's "left"
label1 = tk.Label(row1, text="Enter Goal 1:")
label1.pack(side="left")
goal1entry = tk.Entry(row1)
goal1entry.pack(side= "left")

label2 = tk.Label(row2, text="Enter Goal 2:")
label2.pack(side="left")
goal2entry = tk.Entry(row2)
goal2entry.pack(side="left")

goal1 = tk.StringVar()
goal2 = tk.StringVar()

def update_goals():
    goal1.set(f"Goal 1: {goal1entry.get()}")
    goal2.set(f"Goal 2: {goal2entry.get()}")

enter_button = tk.Button(root, text="Enter Goals", command=update_goals)
enter_button.pack(padx=10, pady=10)

# Create a labelframe to hold widgets
labelframe = tk.LabelFrame(root, text="Your Goals", padx=10, pady=10)
labelframe.pack(padx=10, pady=10)

# Add a label to the labelframe


goal1_in_labelframe = tk.Label(labelframe, textvariable=goal1)
goal1_in_labelframe.pack(side="top")
goal2_in_labelframe = tk.Label(labelframe, textvariable=goal2)
goal2_in_labelframe.pack(side="top")




# Run the application
root.mainloop()
