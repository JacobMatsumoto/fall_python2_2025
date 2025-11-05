import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("400x200")
root.title("Simple calculator")

frame_entry = tk.Frame(root)
frame_entry.pack(padx=10, pady=10)

# setting vars
num1 = tk.IntVar()
num2 = tk.IntVar()
opp = tk.StringVar(value='')
answer = tk.StringVar()
# Making entry fields and radio buttons
entry_1 = tk.Entry(frame_entry, textvariable=num1)
rad_subtract = tk.Radiobutton(
    frame_entry, text="-", variable=opp, value='-')
rad_add = tk.Radiobutton(
    frame_entry, text="+", variable=opp, value='+')
rad_divide = tk.Radiobutton(
    frame_entry, text="/", variable=opp, value='/')
rad_multiply = tk.Radiobutton(
    frame_entry, text="x", variable=opp, value='*')
entry_2 = tk.Entry(frame_entry, textvariable=num2)


def create_equation():
    """
    This function pulls the operator from the radio buttons then it will do the apropriate operation
    using the numbers the user enters and the operator. handles divide by zero and general errors if users enter letters.
    """
    try:
        my_operator = opp.get()

        if my_operator == '-':
            answer.set(num1.get() - num2.get())
        elif my_operator == '+':
            answer.set(num1.get() + num2.get())
        elif my_operator == '/':
            answer.set(num1.get() / num2.get())
        elif my_operator == '*':
            answer.set(num1.get() * num2.get())
        elif my_operator == "":
            answer.set("Please select and operator")

        print(answer.get())
        return answer.get()

    except ZeroDivisionError:
        answer.set("Can not divide by 0")
        return answer.get()

    except Exception as e:  # error handling to print the error as e
        print(e)
        answer.set("Error: Please enter numbers")
        return answer.get()


def show_answer():
    """
    Shows the answer in a show info message box using create equation 
    """
    answer = create_equation()
    messagebox.showinfo("Heres the answer", answer)


get_answer = tk.Button(frame_entry, text="Evaluate", command=show_answer)
get_answer.grid(row=4, column=1, padx=5, pady=5)

entry_1.grid(row=2, column=0, padx=5, pady=5)
rad_add.grid(row=0, column=1, padx=5, pady=5)
rad_subtract.grid(row=1, column=1, padx=5, pady=5)
rad_divide.grid(row=2, column=1, padx=5, pady=5)
rad_multiply.grid(row=3, column=1, padx=5, pady=5)
entry_2.grid(row=2, column=2, padx=5, pady=5)


root.mainloop()
