#Instead of writing same code again and again, you create a function.
def greet():
    print("Hello, welcome to the world of functions!")      
greet()  # Calling the function to execute its code
#output:-
#Hello, welcome to the world of functions!

#Here we can also have different uses with functions
def add_numbers(a, b):
    return a + b    
result = add_numbers(5, 3)  # Calling the function with arguments
print(f"The sum of 5 and 3 is: {result}")
#output:-
#The sum of 5 and 3 is: 8

#Functions with Default Parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}! Welcome to the world of functions!")
greet_user()  # Using default parameter
greet_user("Alice")  # Providing an argument
#output:-
#Hello, Guest! Welcome to the world of functions!
#Hello, Alice! Welcome to the world of functions!
