# ==========================
# Student Management System
# ==========================

students = {}   # Dictionary: key = Roll No, value = {"name": name, "marks": marks}


# Function to safely take integer input
def input_int(prompt):
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        else:
            print("❌ Invalid input! Please enter a valid integer.\n")


# Function to safely take float input (0-100 only)
def input_float(prompt):
    while True:
        val = input(prompt)
        try:
            num = float(val)
            if 0 <= num <= 100:
                return num
            else:
                print("❌ Marks must be between 0 and 100.\n")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")


# Function to safely take name (string only, cleaned properly)
def input_name(prompt):
    while True:
        val = input(prompt)

        # agar sirf spaces diye hain
        if val.isspace() or val == "":
            print("❌ Invalid input! Name cannot be empty or spaces only.\n")
            continue

        val = val.strip()                 # start/end spaces remove
        val = " ".join(val.split())       # multiple spaces -> single space

        if val.replace(" ", "").isalpha():  # sirf alphabets allowed
            return val
        else:
            print("❌ Invalid input! Please enter alphabets only.\n")


# Function to add student
def add_student():
    roll_no = input_int("Enter Roll No: ")

    if roll_no in students:   # ✅ Duplicate check
        print(f"\n❌ Roll No {roll_no} already exists! Please use a different Roll No.\n")
        return   # function yahin stop ho jayega

    name = input_name("Enter Name: ")
    marks = input_float("Enter Marks (0-100): ")

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
    roll_no = input_int("Enter Roll No to search: ")
    if roll_no in students:
        data = students[roll_no]
        grade = calculate_grade(data["marks"])
        print(f"\n🎓 Student Found:\nName: {data['name']}, Marks: {data['marks']}, Grade: {grade}\n")
    else:
        print("\n❌ Student not found!\n")


# Function to delete student
def delete_student():
    roll_no = input_int("Enter Roll No to delete: ")
    if roll_no in students:
        removed = students.pop(roll_no)
        print(f"\n🗑️ Student {removed['name']} removed successfully!\n")
    else:
        print("\n❌ Student not found!\n")


# Function to update student
def update_student():
    roll_no = input_int("Enter Roll No to update: ")
    if roll_no in students:
        print(f"\n✏️ Current Data -> Name: {students[roll_no]['name']}, Marks: {students[roll_no]['marks']}")

        # Name update with validation
        while True:
            name = input("Enter New Name (leave blank to keep same): ")

            if name.strip() == "":   # agar user ne blank chhoda to skip
                break

            if name.isspace():   # sirf spaces diye
                print("⚠️ Invalid name! Cannot be spaces only.\n")
                continue

            name = name.strip()
            name = " ".join(name.split())  # multiple spaces -> single space

            if name.replace(" ", "").isalpha():
                students[roll_no]["name"] = name
                break
            else:
                print("⚠️ Invalid name! Please enter alphabets only.\n")

        # Marks update with validation
        while True:
            marks_input = input("Enter New Marks (leave blank to keep same): ")
            if marks_input.strip() == "":   # user ne blank chhoda
                break
            try:
                marks_val = float(marks_input)
                if 0 <= marks_val <= 100:
                    students[roll_no]["marks"] = marks_val
                    break
                else:
                    print("⚠️ Marks must be between 0 and 100.\n")
            except ValueError:
                print("⚠️ Invalid marks! Please enter a valid number.\n")

        print(f"\n✅ Student {students[roll_no]['name']} updated successfully!\n")
    else:
        print("\n❌ Student not found!\n")


# Main Menu
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

        choice = input("Enter choice: ").strip()   # ✅ spaces remove ho jayengi

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
