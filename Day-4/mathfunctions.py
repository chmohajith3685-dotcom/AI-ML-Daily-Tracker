#here this file will contain all the math-related functions that we want to use in our main program. We can define functions like addition, subtraction, multiplication, and division here. Then we can import this file into our main program and call these functions whenever we need to perform a math operation. This way, we keep our main program clean and organized while still having access to all the necessary math functions.

#Example of a math function in mathfunctions.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."        
    

#here by these we can also call these functions in our main program by importing this file. For example, if we have a main program called "main.py", we can import the mathfunctions module and use the add, subtract, multiply, and divide functions as follows: