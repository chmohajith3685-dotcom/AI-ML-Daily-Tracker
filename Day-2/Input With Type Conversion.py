print("Simple Math Calculator")
print("-" * 20)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."

print("-" * 20)
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")

#output:
#Simple Math Calculator
#--------------------
#Enter the first number: 10
#Enter the second number: 5
#--------------------
#Sum: 15.0
#Difference: 5.0
#Product: 50.0
#Quotient: 2.0
