students = {}
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
        print("Student deleted!")
    else:
        print("Student not found!")
    menu()
def menu():
    print("WELCOME TO SMS")
    print("1. ADD NEW STUDENT")
    print("2. VIEW STUDENT")
    print("3. DELETE STUDENT")
    print("4. EXIST")
    ch = int(input("enter your choice: "))
    if ch == 1:
        add_new()
    elif ch == 2:
        view()
    elif ch == 3:
        delete()
    elif ch == 4:
        print("thank you...!")
    else:
        print("enter valid choice")
        menu()
menu()
