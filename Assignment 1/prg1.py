name = input("Enter Student Name: ")

subjects = ["Tamil", "English", "Maths", "Science", "Computer"]
marks = []

for sub in subjects:
    while True:
        val = float(input(f"Enter marks for {sub}: "))
        if 0 <= val <= 100:
            marks.append(val)
            break
        else:
            print("Invalid marks! Please enter between 0 and 100.")

total = sum(marks)
average = total / len(subjects)

# pass if all subjects >= 35
is_pass = all(m >= 35 for m in marks)
result = "PASS" if is_pass else "FAIL"

if not is_pass:
    grade = "F"
elif average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "E"

print("\n--- Student Result ---")
print(f"Student Name: {name}\n")
for sub, m in zip(subjects, marks):
    print(f"{sub}: {int(m) if m.is_integer() else m}")

print(f"\nTotal: {int(total) if total.is_integer() else total}")
print(f"Average: {average:.1f}")
print(f"Grade: {grade}")
print(f"Result: {result}")
