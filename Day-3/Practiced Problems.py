# Problem 1: Factorial
# Formula: n! = n * (n-1) * ... * 1
import math
num = int(input("\nEnter a number to calculate Factorial: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
#output:-
#Enter a number to calculate Factorial: you need to enter a number
#Factorial of givenn numner is .....


# Problem 2: Fibonacci Sequence
# Sequence: 0, 1, 1, 2, 3, 5, 8... (Next = Prev + PrevPrev)
count = int(input("\nHow many Fibonacci numbers to generate? "))
a, b = 0, 1
print("Fibonacci Sequence:", end=" ")
for _ in range(count):
    print(a, end=" ")
    # Update values: new a becomes old b, new b becomes a + b
    a, b = b, a + b
print()
#output:-
#How many fibonacci numbers to generate ? your number
#fibonacci sequence : .........



# Problem 3: Prime Number Check
num_check = int(input("\nEnter a number to check if Prime: "))
is_prime = True

if num_check <= 1:
    is_prime = False
else:
    # Check divisibility from 2 up to the square root of the number
    for i in range(2, int(math.sqrt(num_check)) + 1):
        if num_check % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num_check} is a Prime Number! ✅")
else:
    print(f"{num_check} is NOT a Prime Number. ❌")

print("\n=== Day 3 Completed Successfully! ===")
#output:-
#Enter a number to check if prime :...
#number is prime/not prime