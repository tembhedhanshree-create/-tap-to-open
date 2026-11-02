students = {
    "101": "Dhanshree Tembhe",
    "102": "Sakshi Patil",
    "103": "Pooja Sharma",
    "104": "Anjali Deshmukh"
}

def add_new():
    name = input("Enter student name: ")
    roll = input("Enter roll no: ")
    students[roll] = name
    print(f"Student {name} added!")
    menu()

def view():
    print("\n--- Student List ---")
    if not students:
        print("No students found!")
    else:
        for roll, name in students.items():
            print(f"Roll: {roll} | Name: {name}")
    print()
    menu()

def delete():
    roll = input("Enter roll no to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted! - Delete Zala")
    else:
        print("Student not found!")
    menu()

def menu():
    print("\n1. ADD Student")
    print("2. VIEW Students")
    print("3. DELETE Student")
    print("4. Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        add_new()
    elif ch == "2":
        view()
    elif ch == "3":
        delete()
    elif ch == "4":
        print("Bye!")
    else:
        print("Invalid choice!")
        menu()

menu()
