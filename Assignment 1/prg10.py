students = [
    {"name": "Arun", "mark": 85},
    {"name": "Priya", "mark": 92},
    {"name": "Kumar", "mark": 67}
]

PASS_MARK = 50

while True:
    print("\n--- Student Management Console ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Find Topper")
    print("6. Display Passed Students")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    match choice:
        case "1":
            name = input("Enter student name: ").strip()
            mark = float(input("Enter student mark (0-100): "))
            if 0 <= mark <= 100:
                students.append({"name": name, "mark": mark})
                print(f"Student '{name}' added successfully.")
            else:
                print("Invalid mark! Must be between 0 and 100.")

        case "2":
            if not students:
                print("No student records found.")
            else:
                print("\nName\t\tMark")
                print("-" * 25)
                for s in students:
                    print(f"{s['name']:<12}\t{s['mark']}")

        case "3":
            search_name = input("Enter name to search: ").strip().lower()
            found = [s for s in students if s["name"].lower() == search_name]
            if found:
                for s in found:
                    status = "Passed" if s["mark"] >= PASS_MARK else "Failed"
                    print(f"Name: {s['name']}, Mark: {s['mark']}, Status: {status}")
            else:
                print("Student not found.")

        case "4":
            if not students:
                print("No records available to calculate average.")
            else:
                avg = sum(s["mark"] for s in students) / len(students)
                print(f"Class Average Mark: {avg:.2f}")

        case "5":
            if not students:
                print("No student records available.")
            else:
                topper = max(students, key=lambda s: s["mark"])
                print(f"Topper: {topper['name']} with {topper['mark']} marks.")

        case "6":
            passed = [s for s in students if s["mark"] >= PASS_MARK]
            if passed:
                print(f"\nPassed Students (>= {PASS_MARK}):")
                for s in passed:
                    print(f"- {s['name']}: {s['mark']}")
            else:
                print("No students have passed.")

        case "7":
            print("Exiting Student Management Console.")
            break

        case _:
            print("Invalid option! Please enter a number between 1 and 7.")
