num = int(input("Enter an integer: "))
n = abs(num)

# digits analysis
digits = [int(d) for d in str(n)]
num_digits = len(digits)
sum_digits = sum(digits)

prod_digits = 1
for d in digits:
    prod_digits *= d

rev_str = str(n)[::-1]
rev_num = int(rev_str) if rev_str else 0
if num < 0:
    rev_num = -rev_num

# even or odd
parity = "Even" if num % 2 == 0 else "Odd"

# prime check
if num <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# palindrome check
is_palindrome = (str(num) == str(num)[::-1])

# armstrong check (sum of each digit raised to power of num_digits)
armstrong_sum = sum(d ** num_digits for d in digits)
is_armstrong = (armstrong_sum == n and num >= 0)

print("\n--- Number Analysis ---")
print(f"Number of digits   : {num_digits}")
print(f"Sum of digits      : {sum_digits}")
print(f"Product of digits  : {prod_digits}")
print(f"Reverse            : {rev_num}")
print(f"Even/Odd           : {parity}")
print(f"Prime status       : {'Prime' if is_prime else 'Not Prime'}")
print(f"Palindrome status  : {'Palindrome' if is_palindrome else 'Not Palindrome'}")
print(f"Armstrong status   : {'Armstrong' if is_armstrong else 'Not Armstrong'}")
