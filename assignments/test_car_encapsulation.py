"""Set Up Your Environment
Create a new Python file for your tests. Name the file test_car_encapsulation.py.

Import the Car Class
Ensure you have the Car class available. If it's in a separate file, import it into your test file.

Write a Test Function for Attribute Access
Write a test function that attempts to directly access and modify the attributes of the Car class. Verify that direct access is not possible.

Write a Test Function for Getters and Setters
Write a test function that uses the getter and setter methods to access and modify the attributes of the Car class. Verify that the getters and setters work as expected.

Write a Test Function for Method Functionality
Write a test function that uses the methods of the Car class to perform actions like adding gas and printing car information. Verify that the methods work as expected.

Run Your Tests
Execute your test file to ensure all tests pass and encapsulation is correctly implemented in the Car class.


AssertionError: Cannot access private attribute '_make' directly
AssertionError: Cannot access private attribute '_model' directly
All tests passed!

    """


class Car:
    def __init__(self, make, model, tank_size, gas_level):
        self._make = make
        self._model = model
        self._tank_size = tank_size
        self._gas_level = gas_level

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def tank_size(self):
        return self._tank_size

    @tank_size.setter
    def tank_size(self, value):
        self._tank_size = value

    @property
    def gas_level(self):
        return self._gas_level

    @gas_level.setter
    def gas_level(self, value):
        if value > self._tank_size:
            self._gas_level = self._tank_size
        else:
            self._gas_level = value

    def add_gas(self, amount):
        if self._gas_level + amount > self._tank_size:
            self._gas_level = self._tank_size
        else:
            self._gas_level += amount

    def car_info(self):
        return f"Make: {self._make}, Model: {self._model}, Tank Size: {self._tank_size} gallons, Gas Level: {self._gas_level} gallons"


# Instantiating the Car class
my_car = Car("Chevrolet", "Corvette", 18, 5)
my_car.add_gas(10)
# Output: Make: Chevrolet, Model: Corvette, Tank Size: 18 gallons, Gas Level: 15 gallons
print(my_car.car_info())
