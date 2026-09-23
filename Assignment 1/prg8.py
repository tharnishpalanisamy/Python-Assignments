def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is Even.")
    else:
        print(f"{n} is Odd.")

def check_prime(n):
    if n <= 1:
        print(f"{n} is Not Prime.")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is Not Prime.")
            return
    print(f"{n} is Prime.")

def check_palindrome(n):
    s = str(abs(n))
    if s == s[::-1]:
        print(f"{n} is a Palindrome.")
    else:
        print(f"{n} is Not a Palindrome.")

def check_armstrong(n):
    if n < 0:
        print(f"{n} is Not an Armstrong number.")
        return
    digits = [int(d) for d in str(n)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    if total == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is Not an Armstrong number.")

def reverse_number(n):
    sign = -1 if n < 0 else 1
    rev = int(str(abs(n))[::-1]) * sign
    print(f"Reverse of {n} is {rev}.")

def sum_of_digits(n):
    total = sum(int(d) for d in str(abs(n)))
    print(f"Sum of digits of {n} is {total}.")

while True:
    print("\n===== NUMBER ANALYZER =====")
    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Check Palindrome")
    print("4. Check Armstrong")
    print("5. Reverse Number")
    print("6. Sum of Digits")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")

    if choice == "7":
        print("Exiting Number Analyzer. Have a great day!")
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        val = int(input("Enter number: "))

        match choice:
            case "1":
                check_even_odd(val)
            case "2":
                check_prime(val)
            case "3":
                check_palindrome(val)
            case "4":
                check_armstrong(val)
            case "5":
                reverse_number(val)
            case "6":
                sum_of_digits(val)
    else:
        print("Invalid choice! Please choose an option between 1 and 7.")
