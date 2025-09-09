"""Create a class named ToyCar with the following attributes:
brand (instance variable)
color (instance variable)
car_type (instance variable)
motorized (instance variable)
toy_type (class variable set to "car")
Use the __init__ method to initialize the brand, color, car_type, and motorized attributes when an instance of ToyCar is created.
Create a method named play that prints "The toy car moves forward.".
Create a method named sound that prints "Vroom".
Create three instances of the ToyCar class:
race_car with brand "Hot Wheels", color "red", type "race car", and motorized set to True.
pickup_truck with brand "Tonka", color "yellow", type "pickup truck", and motorized set to False.
police_car with brand "Matchbox", color "blue", type "police car", and motorized set to True.
Print the class of each instance using the __class__ attribute.
Print the dictionary representation of one of the instances using the __dict__ attribute. """

class ToyCar:
    toy_type = "Car" 

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

    def play(self):
        print(f"The toy car moves forward")

    def sound(self):
        print("Vrooom")


"""race_car with brand "Hot Wheels", color "red", type "race car", and motorized set to True.
pickup_truck with brand "Tonka", color "yellow", type "pickup truck", and motorized set to False.
police_car with brand "Matchbox", color "blue", type "police car", and motorized set to True."""
race_car = ToyCar("Hot Wheels", "red", "race car", True)
pickup_truck = ToyCar("Tonka", "yellow", "pickup truck", False)
police_car = ToyCar("Matchbox", "blue", "police car", True)

print(race_car.__class__)
print(pickup_truck.__class__)
print(police_car.__class__)
print(race_car.__dict__)
print(pickup_truck.__dict__)
print(police_car.__dict__)
