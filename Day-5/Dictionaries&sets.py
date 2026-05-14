print("\n--- 2. Dictionaries & Sets ---")

# --- Dictionaries (Key-Value Pairs) ---
student_profile = {
    "id": 101,
    "name": "Rahul",
    "age": 20,
    "courses": ["Math", "Physics"]
}

print(f"Student Profile: {student_profile}")

# Accessing values
print(f"Student Name: {student_profile['name']}")

# Adding/Updating data
student_profile["grade"] = "A"       # Add new key
student_profile["age"] = 21          # Update existing key
print(f"Updated Profile: {student_profile}")

# Iterating through dictionary
print("\nStudent Details:")
for key, value in student_profile.items():
    print(f"  {key}: {value}")

# --- Sets (Unique Unordered Collection) ---
# Removing duplicates from a list
scores = [85, 90, 85, 70, 90, 95, 70]
unique_scores = set(scores)
print(f"\nOriginal Scores: {scores}")
print(f"Unique Scores: {unique_scores}")

# Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"Union (A | B): {set_a | set_b}")        # All unique elements
print(f"Intersection (A & B): {set_a & set_b}") # Common elements
print(f"Difference (A - B): {set_a - set_b}")   # Elements only in A

"""--- 2. Dictionaries & Sets ---
Student Profile: {'id': 101, 'name': 'Rahul', 'age': 20, 'courses': ['Math', 'Physics']}
Student Name: Rahul
Updated Profile: {'id': 101, 'name': 'Rahul', 'age': 21, 'courses': ['Math', 'Physics'], 'grade': 'A'}

Student Details:
  id: 101
  name: Rahul
  age: 21
  courses: ['Math', 'Physics']
  grade: A

Original Scores: [85, 90, 85, 70, 90, 95, 70]
Unique Scores: {90, 85, 70, 95}
Union (A | B): {1, 2, 3, 4, 5, 6}
Intersection (A & B): {3, 4}
Difference (A - B): {1, 2} """