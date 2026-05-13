#Control Flow Statements (If/Else & Nested Conditions)
import math
#Control Flow Practice

#1.Simple Grading System 
totalscore = input("Enter your total score (0-100): ")
score = int(totalscore)

if score >= 75:
    grade = "A"
    comment = "Excellent"
elif score >= 60:
    grade = "B"
    comment = "Good"
else:
    grade = "C"
    comment = "Needs Improvement"

print(f"Your grade is {grade} with a comment: {comment}")

#2.Nested COnditions - Login Simulation
username = input("\nEnter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "password123":
        print("Login successful! Welcome, admin.")
    else:
        print("Incorrect password. Access denied.")
else:    print("Register first. Access denied.")        
