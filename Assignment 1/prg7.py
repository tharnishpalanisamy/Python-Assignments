import math

n = int(input("Enter a number: "))

def number_of_digits(n):
    res = 0

    while n > 0:
        res += 1
        n //= 10
    return res

def sum_of_digits(n):
    res = 0
    while n > 0:
        digit = n % 10
        res += digit
        n //= 10
    return res


def prod_of_digits(n):
    res = 1
    while n > 0:
        res *= n % 10
        n //= 10
    return res


def reverse_digits(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n //= 10
    return res

def check_palindrome(n):
    reverse = reverse_digits(n)
    return n == reverse

def check_armstrong_number(n) :
    digits = len(str(n))
    x = n
    res = 0
    while x > 0:
        res += (x % 10 ) ** digits
        x //= 10
    return res == n

def check_prime(n) :
    if n < 2 :
        return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return True




print('Results : ')
print(f"----results ------\n"
      f"Number of digits: {number_of_digits(n)}\n"
      f"Sum of Digits: {sum_of_digits(n)}\n "
      f"Product: {prod_of_digits(n)}\n"
      f"Reverse: {reverse_digits(n)}\n"
      f"Even / Odd : {'Even' if n % 2 == 0 else 'Odd'}\n"
      f"Prime : {check_prime(n)}\n"
      f"Palindrome : {check_palindrome(n)} \n"
      f"Armstrong : {check_armstrong_number(n)}\n"  )
