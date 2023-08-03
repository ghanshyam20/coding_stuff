classmates = []

def add_classmate(name):
    classmates.append({'name': name, 'attendance': 0})
    print(f"{name} added to the class")

def make_attendance(name):
    for classmate in classmates:
        if classmate['name'] == name:
            classmate['attendance'] += 1
            print(f"{name} is present. Total attendance: {classmate['attendance']}")
            return
    print("classmate not found.")

def view_attendance():
    print("Attendance")
    for classmate in classmates:
        print(f"{classmate['name']}: {classmate['attendance']}")

def main():
    print("digital attendance system")

    while True:
        print("\noptions")
        print("1. Add classmates")
        print("2. Make attendance")
        print("3. View attendance")
        print("4. Exit")

        choice = input("enter your choice: ")

        if choice == '1':
            name = input("enter classmates name: ").strip()
            add_classmate(name)

        elif choice == '2':
            name = input("enter your classmate name: ").strip()
            make_attendance(name)

        elif choice == '3':
            view_attendance()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
