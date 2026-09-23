student = {
    "id": 101,
    "name": "Karthik",
    "course": "Python",
    "marks": 88
}
print("Initial dictionary:", student)

# accessing values
print("Student Name:", student["name"])
print("Course (using get):", student.get("course"))
print("Grade (default with get):", student.get("grade", "Not Assigned"))

# adding and updating keys
student["grade"] = "A"
student["marks"] = 92
print("After update:", student)

student.update({"city": "Chennai", "marks": 95})
print("After update() method:", student)

# views: keys, values, items
print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# iterating over dictionary
print("\nIterating through items:")
for key, value in student.items():
    print(f"  {key}: {value}")

# membership check
print("\nIs 'course' a key in student?:", "course" in student)
print("Is 'fees' a key in student?:", "fees" in student)

# removing entries
removed_val = student.pop("grade")
print(f"\nPopped 'grade' ({removed_val}):", student)

last_item = student.popitem()
print(f"Popped last item {last_item}:", student)

del student["id"]
print("After del student['id']:", student)

# copying
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# dictionary comprehension
squared_numbers = {x: x * x for x in range(1, 6)}
print("Dict comprehension (number: square):", squared_numbers)

student_copy.clear()
print("After clear():", student_copy)
