"""Create the Address Book Class
Create a class named AddressBook with the following attributes:

first_name
last_name
birthday
email
street_address
city
state
zip
phone
Include getter and setter methods for each attribute.

Implement Magic Methods
Implement at least three magic methods. Some possibilities include:

__str__ - to nicely print the information about each person.
__repr__ - to provide an official string representation of the object.
__eq__ - to compare two AddressBook objects for equality.
Write Docstrings
Include docstrings for your class and its methods to provide documentation. Use the following template:

Class to represent an address book entry.

Attributes:
   include attribute details here

Methods:
   include method details here

Create Instances and Print Information
Create at least four instances of the AddressBook class, each representing a different person. Implement a method to nicely print all the information about each person.
"""


# This is the AddressBook class it contains a lot of information on a person
class AddressBook:
    def __init__(self, first_name, last_name, birthday, email, street_address, city, state, zip_code, phone):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birthday = birthday
        self.__email = email
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip = zip_code
        self.__phone = phone

    # Getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_birthday(self):
        return self.__birthday

    def get_email(self):
        return self.__email

    def get_street_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def get_phone(self):
        return self.__phone

    # Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_birthday(self, birthday):
        self.__birthday = birthday

    def set_email(self, email):
        self.__email = email

    def set_street_address(self, street_address):
        self.__street_address = street_address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip(self, zip_code):
        self.__zip = zip_code

    def set_phone(self, phone):
        self.__phone = phone

    # Methods
    def __str__(self):  # This method augments my print statements for this class making it print the info in a nice and organized way
        return (
            f"First Name: {self.get_first_name()}\n"
            f"Last Name: {self.get_last_name()}\n"
            f"Birthday: {self.get_birthday()}\n"
            f"Email: {self.get_email()}\n"
            f"Address: {self.get_street_address()}\n"
            f"City: {self.get_city()}\n"
            f"State: {self.get_state()}\n"
            f"Zip: {self.get_zip()}\n"
            f"Phone Number: {self.get_phone()}\n"
        )

    def __repr__(self):  # this function retrieves the entry's name and number
        return (
            f"{self.__first_name} {self.__last_name}, {self.__phone}"
        )

    def __eq__(self, other):  # this compares the dict values to return
        # true or false to see if the two addressbook entries are the same
        if self.__dict__ == other.__dict__:
            return True
        else:
            return False


# Making the classed objects
john = AddressBook("John", "Doe", "01/01/1990", "john.doe@example.com",
                   "123 Main St", "Anytown", "NY", "12345", "555-555-5555")

johns_evil_twin = AddressBook("John", "Doe", "01/01/1990", "john.doe@example.com",
                              "123 Main St", "Anytown", "NY", "12345", "555-555-5555")

jane = AddressBook("Jane", "Smith", "02/02/1985", "jane.smith@example.com",
                   "456 Elm St", "Othertown", "CA", "67890", "555-555-1234")

emily = AddressBook("Emily", "Johnson", "03/03/1975", "emily.johnson@example.com",
                    "789 Oak St", "Sometown", "TX", "11111", "555-555-6789")

michael = AddressBook("Michael", "Brown", "04/04/1965", "michael.brown@example.com",
                      "101 Pine St", "Anycity", "FL", "22222", "555-555-2468")

print(john)
print(jane)
print(emily)  # these now print nicely formated full entries
print(michael)


print(repr(john))
# this prints just the name and number the important parts of a phone book
print(john == johns_evil_twin)
# returns true because it compares dict values
print(john == emily)
# returns false because they aren't equal dict values
