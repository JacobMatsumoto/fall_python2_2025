"""
Open your Python development environment:
Start by opening your preferred Python development environment or text editor where you will write your code.

Define the class name:
Decide on a name for your dynamically created class. This will be the first argument to the 'type' function.

Choose the base classes:
Determine if your new class will inherit from any other classes. If so, list these base classes in a tuple. If not, you can use an empty tuple or inherit from 'object'. This will be the second argument to the 'type' function.

Create the methods:
Define at least two methods that your class will have. These methods should be defined as functions in a dictionary, where the keys are the method names and the values are the functions themselves. This dictionary will be the third argument to the 'type' function.

Create the class using 'type':
Use the 'type' function with the class name, base classes tuple, and dictionary of methods to dynamically create your new class.

Instantiate the class:
Create an instance of your new class and call its methods to ensure they work correctly.

Document your code:
Add comments to your code explaining each step and how it works. This will help you and others understand your code better.

Test your code:
Run your code to make sure there are no errors and that it behaves as expected. Make sure both methods are callable and perform their intended actions.

Save your work:
Save your Python file with a meaningful name.

Upload to GitHub:
Navigate to your GitHub directory for the course. Create a new repository or use an existing one, and upload your Python file. Follow the instructions on GitHub to commit and push your changes.

Submit the link:
Once your code is uploaded to GitHub, copy the URL of your repository. Submit this link as your assignment submission.



"""


class CalculatorMeta(type):
    """This meta calculator class makes anything with the metaclass of CalculatorMeta gain addition, 
    subtraction, multiplication, division, and ^ using dct and lambda.
    """
    def __new__(cls, name, bases, dct):
        dct['add'] = lambda self, a, b: a + b
        dct['subtract'] = lambda self, a, b: a - b
        dct['multiply'] = lambda self, a, b: a * b
        dct['divide'] = lambda self, a, b: a / b
        dct['power_of'] = lambda self, a, b: a ** b
        return super().__new__(cls, name, bases, dct)
# https://www.w3schools.com/python/python_lambda.asp


MyCalculator = type('Calculator', (object,), {'add': lambda self, a, b: a + b,
                                              'subtract': lambda self, a, b: a - b,
                                              'multiply': lambda self, a, b: a * b,
                                              'divide': lambda self, a, b: a / b,
                                              'power_of': lambda self, a, b: a ** b
                                              }
                    )
# Above this is making the same calculator class but dynamically on the fly


class MyOtherCalculator(metaclass=CalculatorMeta):
    pass


calculator1 = MyCalculator()  # instantiating the one made with type directly

calculator2 = MyOtherCalculator()  # instantiating the one made via the metaclass


print(calculator1.add(2, 3))
print(calculator1.subtract(10, 4))
print(calculator1.multiply(44, 2))
print(calculator1.divide(222, 2))
print(calculator1.power_of(5, 4))


print(calculator2.add(7, 3))
print(calculator2.subtract(66, 4))
print(calculator2.multiply(4, 2))
print(calculator2.divide(81, 9))
print(calculator2.power_of(7, 3))
