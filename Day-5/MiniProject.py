print("\n--- 3. Mini-Project: Student Grade Tracker ---")
print("Features: Add students, calculate averages, track unique courses.\n")

# Data Structures Used:
# - List: To store the collection of student records
# - Dictionary: To store details of each student (name, grades, avg)
# - Set: To store unique course names across all students

students = []        # List of dictionaries
all_courses = set()  # Set of unique course names

def add_student():
    """Function to add a new student and their grades."""
    print("--- Add New Student ---")
    name = input("Enter student name: ").strip()
    
    # Get courses
    courses_input = input("Enter courses (comma-separated, e.g., Math,Sci): ")
    courses = [c.strip() for c in courses_input.split(",") if c.strip()]
    
    if not courses:
        print("❌ No courses entered. Student not added.")
        return

    # Update the global set of unique courses
    for course in courses:
        all_courses.add(course)
    
    # Get grades for each course
    grades = {}
    for course in courses:
        while True:
            try:
                grade = float(input(f"Enter grade for {course} (0-100): "))
                if 0 <= grade <= 100:
                    grades[course] = grade
                    break
                else:
                    print("   ⚠️ Please enter a number between 0 and 100.")
            except ValueError:
                print("   ⚠️ Invalid input. Please enter a number.")
    
    # Calculate Average
    avg = sum(grades.values()) / len(grades)
    
    # Determine Letter Grade
    if avg >= 90: letter = "A"
    elif avg >= 80: letter = "B"
    elif avg >= 70: letter = "C"
    elif avg >= 60: letter = "D"
    else: letter = "F"
    
    # Create student record
    student_record = {
        "name": name,
        "courses": courses,
        "grades": grades,
        "average": avg,
        "letter": letter
    }
    
    students.append(student_record)
    print(f"✅ Student '{name}' added successfully!")

def display_students():
    """Display all students with their details."""
    print("\n--- All Students ---")
    if not students:
        print("No students recorded yet.")
        return

    for i, student in enumerate(students, 1):
        print(f"\n{i}. {student['name']} ({student['letter']})")
        print(f"   Courses: {', '.join(student['courses'])}")
        print(f"   Grades: {student['grades']}")
        print(f"   Average: {student['average']:.2f}")

def display_courses():
    """Display all unique courses offered."""
    print("\n--- Unique Courses Offered ---")
    if not all_courses:
        print("No courses recorded yet.")
    else:
        print(f"Total Unique Courses: {len(all_courses)}")
        for course in sorted(all_courses):
            print(f" - {course}")

# Main Application Loop
def main():
    while True:
        print("\n=== Student Grade Tracker Menu ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Unique Courses")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            display_courses()
        elif choice == '4':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

print("\n=== Day 5 Completed Successfully! ===")