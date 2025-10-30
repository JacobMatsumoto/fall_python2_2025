"""
    In this assignment, you will combine all the features you've learned so far about Tkinter into a single application. You will create a customized main window, display various message boxes, and use dialog functions to interact with the user. Follow the high-level directions below to complete the assignment.

Assignment Directions
Create the Main Window:
Initialize the main window using Tkinter.
Set a custom title and icon for the window.
Specify the window size and set minimum and maximum size limits.
Implement a close window button that asks for confirmation before closing the window.
Display Message Boxes:
Show an error message box with a custom title and message. done
Show a warning message box with a custom title and message. done
Show an informational message box with a custom title and message. done
Use Dialog Functions:
Implement the askyesno function to ask the user a yes/no question and handle the response. done
Implement the askokcancel function to ask the user an ok/cancel question and handle the response. need
Implement the askretrycancel function to ask the user a retry/cancel question and handle the response. done
Combine Features:
Ensure all the above features are integrated into a single Tkinter application.
Test the application to ensure it works as expected.

Vaguely used the geeks for geeks, mostly used Dave's example file to learn these
https://www.geeksforgeeks.org/python/python-tkinter-askquestion-dialog/
I also used Dave's example file for help on some of these
"""

import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Flip Coin")
root.geometry("500x500")

# centers the main content https://www.pythontutorial.net/tkinter/tkinter-grid/
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


class Coin:
    # coin class. Heads in a row keeps track of how many heads are gotten in a row, face tracks the last face from a flip, the flip built in function is to just flip the coin. odds are 45/45/10 for heads/tails/sideways.
    def __init__(self, heads_in_a_row=0, face="Heads"):
        self.face = face
        self.heads_in_a_row = heads_in_a_row

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value

    def flip(self):
        face = random.randrange(1, 101)

        if face in range(1, 46):  # 45%
            print("Heads!")
            self.heads_in_a_row += 1
            if self.heads_in_a_row > 1:
                print(f"{self.heads_in_a_row} heads in a row!")
            return "Heads"

        elif face in range(46, 56):  # 10%
            print("Sideways?")
            self.heads_in_a_row = 0
            return "Sideways"

        elif face in range(47, 101):
            print("Tails!")  # 45%
            self.heads_in_a_row = 0
            return "Tails"


class MessageBoxes:

    def __init__(self, parent):
        frame = tk.Label(parent)
        frame.grid(row=5, column=1, pady=20)

        # Warning message
        tk.Button(frame, text="Flip the coin 100 times?",
                  command=self.show_warning).grid(row=7, column=1, padx=10, pady=10)

        # Error message
        tk.Button(frame, text="Flip a dollar?",
                  command=self.show_error).grid(row=4, column=1, padx=10, pady=10)

        # Yes/No question
        tk.Button(frame, text="Flip 10 times?",
                  command=self.ask_yes_no).grid(row=5, column=1, padx=10, pady=10)

        # Retry/Cancel
        tk.Button(frame, text="Repeat flips?",
                  command=self.repeatable).grid(row=6, column=1, padx=10, pady=10)

        # ok/cancel
        tk.Button(frame, text="Reset combo", command=self.reset_combo).grid(
            row=8, column=1, padx=10, pady=10)

    def show_info(self):
        messagebox.showinfo("Info", "This is an informational message!")

    def show_warning(self):
        messagebox.showwarning("Warning", "This is going to run 100 times!")
        results = []
        for i in range(101):
            coin_flip = quarter.flip()

            if coin_flip == "Heads" and quarter.heads_in_a_row > 0:
                streak.set(
                    f"Current heads streak: {quarter.heads_in_a_row}")
            # elif quarter.heads_in_a_row >= 5:

            elif coin_flip != "Heads":
                streak.set("Current streak: 0")

            elif coin_flip == "Sideways":
                print("TEMP")

            results.append(coin_flip)

        string_results = ", ".join(results)
        messagebox.showinfo("Here the results:", string_results)

    def show_error(self):
        messagebox.showerror("Error", "We're flipping coins not dollars!")

    def ask_yes_no(self):
        # asks the user if they want to flip the coin 10 times, then it shows the result
        question = messagebox.askyesno(
            "Are you sure?", "This will flip the coin 10 times!")
        if question:
            results = []
            for i in range(11):
                coin_flip = quarter.flip()

                if coin_flip == "Heads" and quarter.heads_in_a_row > 0:
                    streak.set(
                        f"Current heads streak: {quarter.heads_in_a_row}")

                elif coin_flip != "Heads":
                    streak.set("Current streak: 0")

                elif coin_flip == "Sideways":
                    print("TEMP")

                results.append(coin_flip)

            string_results = ", ".join(results)
            messagebox.showinfo("Here the results:", string_results)

        else:
            messagebox.showinfo("Oh well", "Maybe next time!")

    def repeatable(self):
        # same as the top but rapidly repeatable
        while True:
            retry = messagebox.askretrycancel(
                "Retry?", "Do you want to flip the coin 10 times again?"
            )
            if retry == True:
                results = []
                for i in range(11):
                    coin_flip = quarter.flip()

                    if coin_flip == "Heads" and quarter.heads_in_a_row > 0:
                        streak.set(
                            f"Current heads streak: {quarter.heads_in_a_row}")
                    # elif quarter.heads_in_a_row >= 5:

                    elif coin_flip != "Heads":
                        streak.set("Current streak: 0")

                    elif coin_flip == "Sideways":
                        print("TEMP")

                    results.append(coin_flip)

                string_results = ", ".join(results)
                messagebox.showinfo("Here the results:", string_results)
            else:
                messagebox.showinfo("Cancelled", "Maybe we'll flip more later")
                break

    def reset_combo(self):
        answer = messagebox.askokcancel("Reset", "Reset the combo?")
        if answer:
            streak.set("Current streak: 0")
        else:
            messagebox.showinfo("Good Choice!", "Combo preserved")


quarter = Coin()
MessageBoxes(root)
result = tk.StringVar()
streak = tk.StringVar()

result.set("Flip the coin!")
streak.set("Get a streak of heads in a row!")


def flip_coin():
    coin_flip = quarter.flip()
    result.set(f"Result: {coin_flip}")
    if coin_flip == "Heads" and quarter.heads_in_a_row > 0:
        streak.set(f"Current heads streak: {quarter.heads_in_a_row}")
    # elif quarter.heads_in_a_row >= 5:

    elif coin_flip != "Heads":
        streak.set("Current streak: 0")

    elif coin_flip == "Sideways":
        print("TEMP")


flip_result = tk.Label(root, textvariable=result, width=25, anchor="center")


current_streak = tk.Label(root, textvariable=streak,
                          width=25, anchor="center")

flip_button = tk.Button(root, text="Flip the coin!",
                        command=flip_coin, anchor="center")

empty_left = tk.Label(root)
empty_right = tk.Label(root)


flip_button.grid(row=3, column=1, padx=10, pady=10)
current_streak.grid(row=2, column=1, padx=10, pady=10)
flip_result.grid(row=1, column=1, padx=10, pady=10)


root.mainloop()
