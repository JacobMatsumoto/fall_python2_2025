"""
    _summary_
    CRUD - Create, Read, Update, Delete


"""


def menu(customer):
    try:
        print("Greetings! What would like to do do today?")
        choice = 0
        while choice != 5:
            # menu will display options, accept a number, then call the function
            print("1.  Search for and display a record.")
            print("2.  Create a new record.")
            print("3.  Update an existing record")
            print("4.  Delete an existing record")
            print("5.  Quit the program.")
            choice = int(input("Please enter the number of your selection: "))
            if choice == 1:
                display(customer)
            elif choice == 2:
                create(customer)
            elif choice == 3:
                update(customer)
            elif choice == 4:
                delete(customer)
            elif choice == 5:
                print("Goodbye!")
            else:
                print("I don't understand!")

    except Exception as e:
        print("Invalid! ", e)


def check():
    try:
        with open("data.txt", 'r') as file:
            customers = file.readlines()
            return customers
    except FileNotFoundError:
        customers = []
        return customers
    except Exception as e:
        print("Unsuccessfull: ", e)


def create(customers):
    # create a new record, call the save function and save to the external file.
    print("Create a new record!")
    f_name = input("Please enter the first name: ").capitalize()
    l_name = input("Please enter the last name: ").capitalize()
    email = input("Please enter the email:  ")
    record = f_name + "," + l_name + "," + email + "\n"
    customers.append(record)
    # print(customers)
    save(customers)


# def read(customers):
#     print("read")
#  optionall approach instead of passing around the list
#  Project Creep


def update(customers):
    try:
        print("We will update an existing record. ")
        account = find(customers)
        changeme = customers[account].split(",")
        for item in changeme:
            print(item)

        if (type(account)) == int:
            print("int")
            print("Account Found!")
            print(f"The record is: {customers[account]}")
        else:
            print(f"Record not found!\n{account}")

        # menu for changing item
        choice = 8
        while not (0 < choice < 4):
            print(
                "Enter 1 to Change First Name\nEnter 2 to Change Last Name\nEnter 3 to Change Email")
            choice = int(
                input("Please enter the number of the value that you want to change "))

            if choice == 1:
                fname = input("Please enter the new first name  ")
                changeme[0] = fname
                choice = 1
            elif choice == 2:
                lname = input("Please enter the new last name  ")
                changeme[1] = lname
                choice = 2
            elif choice == 3:
                email = input("Please enter the new email  ")
                changeme[2] = email
                choice = 3
            else:
                print("that is not a valid input")
                choice = 8

        change = ",".join(changeme)
        print(change, "Is the updated record.")
        customers[account] = change
        save(customers)

    except Exception as e:
        print("Not a valid menu choice, ", e)


def delete(customers):  # I mostly copy pasted my update code here because it uses a similar settup
    # call find, get index
    # pop index
    # call save passing customer
    try:
        print("Let's will delete an existing record. ")
        account = find(customers)

        if (type(account)) == int:
            print("int")
            print("Account Found!")
            print(f"The record is: {customers[account]}")
        else:
            print(f"Record not found!\n{account}")

        # menu for deleting item
        choice = 8
        while not (choice == 'No' or choice == 'Yes'):
            print("Are you sure you want to delete this file? enter 'Yes' or 'No")
            choice = input("Please enter Yes or No ").title()

            if choice == 'Yes':
                customers.pop(account)
                print('account deleted')
                save(customers)
                choice = 'Yes'

            elif choice == 'No':
                print("Deletion stopped")
                choice = 'No'

            else:
                print("that is not a valid input")
                choice = 8

    except Exception as e:
        print("Not a valid menu choice, ", e)


def find(customers):
    # find a customer, return the index of the customer
    # search by phone number
    # return index
    # TODO Note: in VERSION 2 - allow searching by last name
    print("Let me look for that record for you.")
    email = input("Please enter the email you want to look for. ")
    my_index = 0
    for line in customers:
        line = line.strip("\n")
        record = line.split(',')

        if record[2] == email:
            print("Found!", line)
            return my_index
        else:
            my_index += 1
    print("\n\nRecord not found for email: ", email)
    return "I'm sorry, that record does not exist\n\n"


def display(customers):
    find(customers)


def save(customers):
    # called any time a change is made
    # writes the customers list to the data.txt file
    try:
        with open("data.txt", "w") as file:
            for line in customers:
                file.write(line)
        file.close()
        print(customers)
        print("Successfully saved.")
    except Exception as e:
        print("Oops. That didn't work!", e)


def main():
    # menu for user
    # customer will be the list of customer records
    customer = check()  # Does the file exist? If yes, copy to list, if no, create list
    print(customer)
    menu(customer)


main()
