# import tkinter as tk

# root = tk.Tk()

# # Create label widgets
# label1 = tk.Label(root, text="Label 1")
# label2 = tk.Label(root, text="Label 2")
# label3 = tk.Label(root, text="Label 3")

# # Place labels in the grid
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=1)
# label3.grid(row=2, column=0, columnspan=2)  # Span across two columns

# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.title("Sample")

name = tk.Label(root, text="First Name:")
entry_name = tk.Entry(root, width=20)

email = tk.Label(root, text="Email:")
entry_email = tk.Entry(root, width=20)

password = tk.Label(root, text="Password:")
entry_password = tk.Entry(root, width=20)


name.grid(row=0, padx=5, pady=5, column=0,)
entry_name.grid(row=0, padx=5, pady=5, column=1)

email.grid(row=1, padx=5, pady=5, column=0,)
entry_email.grid(row=1, padx=5, pady=5, column=1)

password.grid(row=2, padx=5, pady=5, column=0,)
entry_password.grid(row=2, padx=5, pady=5, column=1)


root.mainloop()