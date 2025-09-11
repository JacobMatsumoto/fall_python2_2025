"""
Assignment Instructions
Create a Python function named conference_signup that accepts any number of participant names using *args and their contact details (email and phone) using **kwargs.
Inside the function, print a summary of the participants and their contact details in a clear and organized format.
Ensure that your function handles cases where no participants or no contact details are provided gracefully.
Test your function with sample data to ensure it works correctly.
"""

"""
this takes a tuple of names to print out each individually, it also takes a dictionary where the dictionary can hold 
either a tuple or a single value. it also handles a valueless dictionary key and pushes an error for it. 
the primary purpose of this is to take a tuple of people and a dictionary of their contact info in order to print
who is attending and then also how to contact them if they gave the contact info.
"""


def conf_sign_ups(*people, **contacts):
    print("People attending:")
    for person in people:
        print(person)

    print("\nPeople's contact info:")
    for name, info in contacts.items():  # This makes name = the key of the dictionary and info what the key's held values
        try:
            if info == ():  # If info is an empty tuple it raises a value error to kick it down to my exception checker
                raise ValueError
            if len(info) == 2:
                print(  # I could theoretically make this use the same logic as the elif info.replace.isdigit and if @ is in info to format if email or phone number come first but that is extra project creep.
                    # Tony Helped me with formatting this
                    f"----------------------------------------\n"
                    f"Name: {name}\n"
                    # info[0] is the first item in the tuple
                    f"Phone number: {info[0]}\n"
                    # info[1]is printing the second item in the tuple
                    f"Email: {info[1]}\n"
                    f"-----------------------------------------"
                )
            # this replaces the -'s in a phone number with empty space and then checks if it is all numbers
            elif info.replace("-", "").isdigit():
                print(
                    # Tony Helped me with formatting this
                    f"-----------------------------------------\n"
                    f"Name: {name}\n"
                    f"Phone Number: {info}\n"
                    f"-----------------------------------------"
                )
            # all emails must contain an @ so this checks to see if its an email.
            elif "@" in info:
                # Tony Helped me with formatting this
                print(
                    f"-----------------------------------------\n"
                    f"Name: {name}\n"
                    f"Email: {info}\n"
                    f"-----------------------------------------"
                )
        except ValueError as e:
            print(
                f"-----------------------------------------\n"
                f"ERROR {name} has no contact info {e}\n"
                f"-----------------------------------------"
            )


attendees = ("Jim", "Carla", "James", "Bob", "Jil")

contact_info = {
    "Jim": ("999-222-1212", "jim@test.com"),
    "Carla": ("299-233-1222", "carla@gmal.com"),
    "James": ("444-444-4444"),  # only a phone number
    # below is only an email, and tests to make sure the phone number check can differentiate numbers and emails. it can.
    "Bob": ("4343-o@gma.com"),
    "Jil": ()  # no contact info
}

conf_sign_ups(*attendees, **contact_info)
