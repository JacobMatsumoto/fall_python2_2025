

def menu():
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
                print("Invalid input")

    except Exception as e:
        print("Invalid! ", e)
