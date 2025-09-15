"""
Create a Class
Define a class with a meaningful name related to your scenario (e.g., Duck, Car, Student).
Define Instance Variables
Inside the class, define the __init__ method to initialize instance variables.
Create at least two instance variables to store specific information about the object.
Implement Instance Methods
Define at least one instance method that operates on instance variables.
Ensure the method modifies or utilizes instance variables in some way.
Remember to include self as the first parameter.
Implement Class Methods
Use the @classmethod decorator to define at least one class method.
Ensure the method modifies or utilizes class variables.
Remember to include cls as the first parameter.
Implement Static Methods
Use the @staticmethod decorator to define at least one static method.
Ensure the method performs a utility function related to the class but does not modify instance or class variables.
Static methods do not need self or cls parameters.
Create Instances
Outside the class, create multiple instances of the class to demonstrate the instance methods.
Call the instance methods on these objects and print the results.
Demonstrate Class Methods
Call the class methods directly on the class itself and print the results.
Show how the class method affects all class instances, if applicable.
Demonstrate Static Methods
Call the static method directly on the class and print the results.
Explain how the static method is used for utility functions related to the class.
Test and Document
Test the program to ensure all methods work as expected.
Add comments to the code to explain what each method does and how it is used.
Write a brief explanation at the end of the program to summarize the differences between instance methods, class methods, and static methods. This can be in a doc string comment  between 3 sets of quotes.
Submit Your Work
Upload your finished program to your GitHub directory.
Provide the link to your instructor for review.
"""
#decided to just grab toy car from a previous assignment and add to it

class ToyCar:
    toy_type = "Car"
    sticker = "Super Man stickers"
    def __init__(self, brand, color, car_type, motorized):
        self.__brand = brand
        self.__color = color
        self.__car_type = car_type
        self.__motorized = motorized

    def get_brand(self):
        return self.__brand

    def get_color(self):
        return self.__color

    def get_car_type(self):
        return self.__car_type

    def get_motorized(self):
        return self.__motorized

    def set_brand(self, value):
        self.__brand = value

    def set_color(self, value):
        self.__color = value

    def set_car_type(self, value):
        self.__car_type = value

    def set_motorized(self, value):
        self.__motorized = value

    def play(self): #changing this slightly
        return f"The {self.__car_type} moves forward" #instance method to grab the type of car saying it goes forward
        

    def sound(self):
        print("Vrooom")

    @classmethod
    def set_sticker(cls, sticker):
        cls.sticker = sticker 

    @staticmethod
    def is_cool():
        return f"Ya darn right it's cool!"

#creating instances
race_car = ToyCar("Hot Wheels", "red", "race car", True)
pickup_truck = ToyCar("Tonka", "yellow", "pickup truck", False)
police_car = ToyCar("Matchbox", "blue", "police car", True)

print(pickup_truck.sticker)
ToyCar.set_sticker("Batman sticker") # changes the "stickers" on all the objects 
#in toycar using the class method and changes all their stickers
print(pickup_truck.sticker) 

print(race_car.play()) #using the play instance method

print(police_car.is_cool())  # prints Ya darn right it's cool! from the static method

"""
Static methods are for utility related to the class and don't need access to class features
Instance methods are used on instances of classed objects and needs a self parameter, which it refers to from the classed object
Class methods are tied to the class and can modify the all shared classed objects
"""