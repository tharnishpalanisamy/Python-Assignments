s1 = {1, 2, 3, 4, 5, 2, 3}
print("Initial set s1 (duplicates removed):", s1)

# adding elements
s1.add(6)
print("After add(6):", s1)

s1.update([7, 8, 9])
print("After update([7, 8, 9]):", s1)

# removing elements
s1.remove(9)
print("After remove(9):", s1)

s1.discard(100)  # doesn't throw error if not present
print("After discard(100):", s1)

removed_item = s1.pop()
print(f"Popped item: {removed_item}, set after pop():", s1)

# set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("\nSet A:", a)
print("Set B:", b)
print("Union (A | B):", a.union(b))
print("Intersection (A & B):", a.intersection(b))
print("Difference (A - B):", a.difference(b))
print("Difference (B - A):", b.difference(a))
print("Symmetric Difference (A ^ B):", a.symmetric_difference(b))

# relational checks
sub = {1, 2}
print("\nIs {1, 2} subset of A?:", sub.issubset(a))
print("Is A superset of {1, 2}?:", a.issuperset(sub))
print("Are A and {9, 10} disjoint?:", a.isdisjoint({9, 10}))

# membership check
print("Is 3 in Set A?:", 3 in a)
print("Is 10 in Set A?:", 10 in a)

copy_set = a.copy()
print("Copied set:", copy_set)

copy_set.clear()
print("After clear():", copy_set)
