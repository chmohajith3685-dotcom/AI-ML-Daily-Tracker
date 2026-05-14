""" Day 5 : Data Structures """
# lists, tuples, dictionaries and sets

print("1.Lists and tuples")

fruits = ["apple", "banana", "orange", "mango" ]
print(f"Original list: {fruits}")
#Original list: ['apple', 'banana', 'orange', 'mango']

#accessing elements
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
#First item: apple
#Last item: mango

#slicing (getting a portion of list)
print(f"First two items: {fruits[:2]}")
#First two items: ['apple', 'banana']

#manipulating the list
fruits.append("elderberry")               #add to end
print(f"After append: {fruits}")
#After append: ['apple', 'banana', 'orange', 'mango', 'elderberry']

fruits.insert(1, "apricot")           #insert index at 1
print(f"After insert: {fruits}")
#After insert: ['apple', 'apricot', 'banana', 'orange', 'mango', 'elderberry']

fruits.remove("banana")
print(f"After remove: {fruits}")       #remove by the value
#After remove: ['apple', 'apricot', 'orange', 'mango', 'elderberry']

fruits.sort()
print(f"Sorted list{fruits}")
#Sorted list['apple', 'apricot', 'elderberry', 'mango', 'orange']

# --- Tuples (Immutable Ordered Collection) ---
# Coordinates that should never change
location = (12.9716, 77.5946)
print(f"\nLocation Coordinates: {location}")
#Location Coordinates: (12.9716, 77.5946)

# Unpacking a tuple
lat, lon = location
print(f"Latitude: {lat}, Longitude: {lon}")
#Latitude: 12.9716, Longitude: 77.5946