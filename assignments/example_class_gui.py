# Import the Tkinter library
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Weight Converter")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Add a label and input field for the amount
amount_label = tk.Label(frame, text="Enter the amount:")
amount_label.pack()
amount_entry = tk.Entry(frame)
amount_entry.pack()

# Add radio buttons for conversion type
conversion_type = tk.StringVar(value="lb_to_kg")
lb_to_kg_radio = tk.Radiobutton(
    frame, text="Pounds to Kilograms", variable=conversion_type, value="lb_to_kg")
lb_to_kg_radio.pack()
kg_to_lb_radio = tk.Radiobutton(
    frame, text="Kilograms to Pounds", variable=conversion_type, value="kg_to_lb")
kg_to_lb_radio.pack()

kg_to_lb_radio = tk.Radiobutton(
    frame, text="Kilograms to Tonnes", variable=conversion_type, value="K2T")
kg_to_lb_radio.pack()

kg_to_lb_radio = tk.Radiobutton(
    frame, text="Pounds to Tonnes", variable=conversion_type, value="P2T")
kg_to_lb_radio.pack()
# Add a calculate button


def calculate():
    try:
        amount = float(amount_entry.get())

        if conversion_type.get() == "lb_to_kg":
            result = amount * 0.453592
            result_label.config(text=f"{amount} lbs is {result:.2f} kg")

        elif conversion_type.get() == "kg_to_kg":
            result = amount / 0.453592
            result_label.config(text=f"{amount} kg is {result:.2f} lbs")

        elif conversion_type.get() == "K2T":
            result = amount * 0.001
            result_label.config(text=f"{amount} kg is {result:.2f} ~tonnes")
        else:
            result = amount * 0.0004535924
            result_label.config(text=f"{amount} lbs is {result:.2f} ~tonnes")

    except ValueError:
        result_label.config(text="Please enter a valid number")


calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.pack()

# Add a label to display the result
result_label = tk.Label(frame, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
