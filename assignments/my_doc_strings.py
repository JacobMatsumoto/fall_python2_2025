
#TODO add some extra opporations, factorial maybe?
class Calculator:
    "This Calculator class encapsulates some basic math opporations, you can make calculator objects and they can use the opporations"
    def __init__(self, value=0): 
        #innitializes whatever you give the Calculator class as a value 0 number 
        self.value = value

    def add(self, num):
        self.value += num #addition

    def subtract(self, num):
        self.value -= num #subtraction

    def multiply(self, num):
        self.value *= num #multiplication

    def divide(self, num):
        # TODO this should be if num != 0 and self.value != 0 then divide. as this still allows value to be zero
        if num != 0: 
            self.value /= num #division error checking preventing divide by zero errors
        else:
            raise ValueError("Cannot divide by zero") #if num is 0 it raises an error

    def clear(self):  
        # resets the value to zero
        self.value = 0 

    def get_value(self):
        # returns it's value
        return self.value

 
def main():
    """This main function makes a Calculator object and tests out its ability to do each of the basic opporations allowed by the Calculator class"""
    calc = Calculator() #makes "calc" have the Calculator class
    calc.add(10) # addition + calc value = 10
    calc.subtract(2) #subtraction - calc value = 8
    calc.multiply(5) # multiplication * calc value = 40
    """This try except block checks to see if the if else works from the divide function"""
    try:
        calc.divide(0)
    except ValueError as e: #error handling to print the error as e
        print(e)
    calc.divide(4) #division / calc is now 10 again
    #TODO include use of .clear()
    print(f"Final value: {calc.get_value()}") 


if __name__ == "__main__":
    """This makes sure this is only ran if called/executed directly"""
    main()
help(Calculator)
