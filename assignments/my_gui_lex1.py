import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Data Entry Form")

# Create frames
frame_entry = tk.Frame(root)
frame_buttons = tk.Frame(root)

frame_entry.grid(row=0, column=0, padx=10, pady=10)
frame_buttons.grid(row=1, column=0, padx=10, pady=10)

# Name
label_name = tk.Label(frame_entry, text="Name:")
entry_name = tk.Entry(frame_entry)

label_name.grid(row=0, column=0, sticky='w')
entry_name.grid(row=0, column=1)

# Email
label_email = tk.Label(frame_entry, text="Email:")
entry_email = tk.Entry(frame_entry)

label_email.grid(row=1, column=0, sticky='w')
entry_email.grid(row=1, column=1)

# Phone
label_phone = tk.Label(frame_entry, text="Phone:")
entry_phone = tk.Entry(frame_entry)

label_phone.grid(row=2, column=0, sticky='w')
entry_phone.grid(row=2, column=1)

# Address
label_address = tk.Label(frame_entry, text="Address:")
entry_address = tk.Entry(frame_entry)

label_address.grid(row=3, column=0, sticky='w')
entry_address.grid(row=3, column=1)

# Phone type checkboxes
label_phone_type = tk.Label(frame_entry, text="Phone Type:")
phone_type_var = tk.StringVar(value='')
checkbox_home = tk.Radiobutton(
    frame_entry, text="Home", variable=phone_type_var, value='Home')
checkbox_mobile = tk.Radiobutton(
    frame_entry, text="Mobile", variable=phone_type_var, value='Mobile')
#!Important I tried fixing both appearing selected at launch but I can't fix it. If you know how I could have can you add it to a comment please?
label_phone_type.grid(row=4, column=0, sticky='w')
checkbox_home.grid(row=4, column=1, sticky='w')
checkbox_mobile.grid(row=4, column=2, sticky='w')

# display entered


def display_info():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    phone_type = phone_type_var.get()
    messagebox.showinfo(
        "Information", f"Name: {name}\nEmail: {email}\nPhone: {phone} ({phone_type})\nAddress: ({address})")


# buttons
button_display = tk.Button(
    frame_buttons, text="Display Information", command=display_info)
button_quit = tk.Button(frame_buttons, text="Quit", command=root.destroy)

button_display.grid(row=0, column=0, padx=5, pady=5)
button_quit.grid(row=0, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
