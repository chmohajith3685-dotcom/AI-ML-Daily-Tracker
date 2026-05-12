#arithmetic operators demo
a = 89
b = 29
print("Arithmetic Operators Demo")
print(f"Numbers: {a} and {b}")
print("-" * 20)

print(f"Addition (+):   {a + b}")
print(f"Subtraction (-): {a - b}")
print(f"Multiplication (*): {a * b}")
print(f"Division (/): {a / b}")
print(f"Floor Division (//): {a // b}")
print(f"Modulus (%):   {a % b}")
print(f"Exponent (**): {a ** b} ")

#output:
#Arithmetic Operators Demo
#Numbers: 89 and 29
#--------------------
#Addition (+):   118
#Subtraction (-): 60
#Multiplication (*): 2581
#Division (/): 3.0689655172413794
#Floor Division (//): 3
#Modulus (%):   2
#Exponent (**): 340651411429620863298662023897395799083174320825636870009

# comparison_demo.py

x = 15
y = 20

print("Comparison Operators Demo")
print(f"Comparing {x} and {y}")
print("-" * 20)

print(f"{x} == {y}  (Equal):      {x == y}")
print(f"{x} != {y}  (Not Equal):  {x != y}")
print(f"{x} > {y}   (Greater):    {x > y}")
print(f"{x} < {y}   (Less):       {x < y}")
print(f"{x} >= 15   (Greater/Equal): {x >= 15}")
print(f"{y} <= 20   (Less/Equal): {y <= 20}")

#output:
#Comparison Operators Demo
#Comparing 15 and 20
#--------------------
#15 == 20  (Equal):      False
#15 != 20  (Not Equal):  True
#15 > 20   (Greater):    False
#15 < 20   (Less):       True
#15 >= 15   (Greater/Equal): True
#20 <= 20   (Less/Equal): True

# assignment_demo.py

score = 100
print(f"Starting Score: {score}")
print("-" * 20)

score += 10   # Add 10
print(f"After += 10: {score}")

score -= 5    # Subtract 5
print(f"After -= 5:  {score}")

score *= 2    # Multiply by 2
print(f"After *= 2:  {score}")

score /= 4    # Divide by 4
print(f"After /= 4:  {score}")

score %= 3    # Modulus (remainder of division by 3)
print(f"After %= 3:  {score}")

#output:
#Starting Score: 100
#--------------------
#After += 10: 110
#After -= 5:  105
#After *= 2:  210
#After /= 4:  52.5
#After %= 3:  1.5
