
#Loops (For & While)
#1.For Loop with Range (Counting)
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  Count: {i}")
#output :Counting from 1 to 5:
 # Count: 1
 # Count: 2
 # Count: 3
 # Count: 4
 # Count: 5


#2.For Loop with List
fruits = ["apple", "banana", "cherry"]
print("\nFruit List:")
for fruit in fruits:
    print(f"  - {fruit}")
#output :
#Fruit List:
 #- apple
 #- banana
 # - cherry

#3.While Loop (User Input Loop)
print("\nWhile Loop: Type 'quit' to stop.")
while True:
    user_text = input("Say something: ")
    if user_text.lower() == "quit":
        print("Loop ended.")
        break
    print(f"  You said: {user_text}")
#output :-
#While Loop: Type 'quit' to stop.
#Say something: 

