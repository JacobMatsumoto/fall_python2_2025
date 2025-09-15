"""
Define the Class-based Decorator:
Create a class called TimingDecorator with an __init__ method that takes a function as an argument and stores it as an instance variable.

Implement the __call__ Method:
Define the __call__ method within the TimingDecorator class. This method should:

Record the start time.
Call the stored function with its arguments.
Record the end time.
Print the execution time.
Return the result of the function call.
Create a Computationally Intensive Function:
Write a function that performs a computationally intensive task, such as calculating the factorial of a large number.

Apply the Decorator:
Apply the TimingDecorator to the computationally intensive function using the @ syntax.

Test the Decorated Function:
Call the decorated function with a large input value to observe the execution time.

Experiment with Different Functions:
Try applying the TimingDecorator to other functions to see how it works with different computational tasks.
"""

import time #importing time to have access to the ability to time the functions


class TimerDecorator:  # this records the time it takes for a function to run and prints it
    def __init__(self, function): #grabs the function it's used on
        self.function = function

    def __call__(self, *args, **kwargs): # this augments the __call__ magic method that happens to anything with this class as a decorator to also contain the function of calculation the time it takes to run the function
        
        start_timer = time.perf_counter()  # this records the start time 
        # https://www.geeksforgeeks.org/python/time-perf_counter-function-in-python/ source for how to record time how i think it wanted
        # calling the function it's being used on
        function_results = self.function(*args, **kwargs)
        end_timer = time.perf_counter()  # records the end time
        total_time = end_timer - start_timer  # retrieves time elapsed

        # print(f"Execution Time: {total_time:.4f} seconds") #prints time elapsed
        # the project only wanted .4f but i made it .6f because it took doing 999 factorial to get it to finally show 0.0002 seconds and the number muddys up the result in terminal
        print(f"Execution Time: {total_time:.6f} seconds")
        return function_results  # returns what the function did.


@TimerDecorator
def factorial(number):  # this function just does factorials
    if number == 0 or number == 1:  # catches if the number is 0! or 1! because those just result in 1
        return 1
    result = 1  # nulifys first multiplication
    # for numbers in the range of 1 and our starting number + 1. so in this case its 1-6 multiplying by 2-5
    for num in range(1, number + 1):
        result *= num  # multiply the result by the number it is at, in this case it's 5, so it does 2, 3, 4, then 5
    return result


print(factorial(5))
