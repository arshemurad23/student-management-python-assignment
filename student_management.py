# Student Management System

students = {}   # Dictionary: key = Roll No, value = {"name": name, "marks": marks}

# Function to add student
def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    
    students[roll_no] = {"name": name, "marks": marks}
    print(f"\n✅ Student {name} added successfully!\n")

# Function to view all students
def view_students():
    if not students:
        print("\n⚠️ No students found!\n")
    else:
        print("\n📋 Student List:")
        for roll, data in students.items():
            print(f"Roll No: {roll}, Name: {data['name']}, Marks: {data['marks']}")
    print()

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

# Function to view specific student
def view_student():
    roll_no = input("Enter Roll No to search: ")
    if roll_no in students:
        data = students[roll_no]
        grade = calculate_grade(data["marks"])
        print(f"\n🎓 Student Found:\nName: {data['name']}, Marks: {data['marks']}, Grade: {grade}\n")
    else:
        print("\n❌ Student not found!\n")

# Function to delete student
def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    if roll_no in students:
        removed = students.pop(roll_no)
        print(f"\n🗑️ Student {removed['name']} removed successfully!\n")
    else:
        print("\n❌ Student not found!\n")

# Function to update student
def update_student():
    roll_no = input("Enter Roll No to update: ")
    if roll_no in students:
        print(f"\n✏️ Current Data -> Name: {students[roll_no]['name']}, Marks: {students[roll_no]['marks']}")
        name = input("Enter New Name (leave blank to keep same): ")
        marks_input = input("Enter New Marks (leave blank to keep same): ")

        # Agar name blank hai to purana name hi rahe
        if name.strip() != "":
            students[roll_no]["name"] = name

        # Agar marks blank nahi hai to int mai convert karke update karein
        if marks_input.strip() != "":
            students[roll_no]["marks"] = int(marks_input)

        print(f"\n✅ Student {students[roll_no]['name']} updated successfully!\n")
    else:
        print("\n❌ Student not found!\n")

# Main Menu
def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Specific Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            view_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("\n👋 Exiting... Thank you!")
            break
        else:
            print("\n⚠️ Invalid Choice! Try again.\n")

# Run the program
menu()
