#1.Countdown 
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)
#output:-
#5
#4
#3
#2
#1

#2.Factorial usimg recursion
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
#output:-
#120

#3.Sum of numbers
def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)

print(total(5))
#output :-
#15

#where recursive function means the function calls itself 
#base case means stopping the condition
#recursive call means function calling itself.