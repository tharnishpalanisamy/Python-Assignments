numbers = [10, 25, 30, 45, 25, 60]
print("Initial list:", numbers)

# accessing and slicing
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])

# adding elements
numbers.append(70)
print("After append(70):", numbers)

numbers.insert(2, 99)
print("After insert(2, 99):", numbers)

numbers.extend([80, 90])
print("After extend([80, 90]):", numbers)

# removing elements
numbers.remove(25)
print("After remove(25):", numbers)

popped = numbers.pop()
print(f"Popped element: {popped}, List after pop():", numbers)

popped_at = numbers.pop(1)
print(f"Popped at index 1: {popped_at}, List:", numbers)

# searching and counting
print("Index of 60:", numbers.index(60))
print("Count of 25:", numbers.count(25))

# sorting and reversing
numbers.reverse()
print("After reverse():", numbers)

numbers.sort()
print("After sort():", numbers)

numbers.sort(reverse=True)
print("After descending sort():", numbers)

# built-in functions
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# copying
copy_list = numbers.copy()
print("Copied list:", copy_list)

# list comprehension
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print("List comprehension (squares 1-5):", squares)

numbers.clear()
print("After clear():", numbers)
