
# Basic if-else and grade checking
if a >= 90 and a <= 100:
    print("Grade A")
elif a >= 80 and a <= 89:
    print("Grade B")
elif a >= 70 and a <= 79:
    print("Grade C")
elif a >= 60 and a <= 69:
    print("Grade D")
else:
    print("Grade F")

# Leap year check
year = int(input("Enter the year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Palindrome check (string)
text = input()
cleaned = ""
for char in text:
    if char not in string.punctuation:
        cleaned += char
cleaned = cleaned.lower().replace(" ", "")
if cleaned == cleaned[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

# Factorial using for loop
a = 5
result = 1
for i in range(1, a + 1):
    result *= i
print(result)

# Factorial using while loop
a = 5
result = 1
i = 1
while i <= a:
    result *= i
    i += 1
print(result)

# Sum of digits
a = int(input())
sums = 0
while a > 0:
    b = a % 10
    sums += b
    a = a // 10
print(sums)

# Multiplication table
a = int(input())
for i in range(1, 11):
    result = a * i
    print(result)

# Count digits
a = int(input())
a = str(a)
count = len(a)
print(count)

# Print stars pattern
a = int(input())
for i in range(1, a + 1):
    print("*" * i)

# Prime number check (corrected)
a = int(input())
is_prime = True
if a <= 1:
    is_prime = False
else:
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break
if is_prime:
    print("It is a prime number")
else:
    print("It is not a prime number")

# FizzBuzz
n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Function examples
def addsum(a, b):
    return a + b
print(addsum(6, 7))

def square(a):
    return a * a
print(square(6))

def evenoddcheck(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
evenoddcheck(13)

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))

# Palindrome function
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
print(is_palindrome("madam"))

# List processing
a = [2, 5, 7, 8, 4]
sum_total = 0
for i in range(len(a)):
    print(a[i])
    sum_total += a[i]
print(sum_total)

# Find max in list
def find_max(a):
    l = len(a)
    check = a[0]
    for i in range(l):
        if a[i] > check:
            check = a[i]
    return check
print(find_max([34, 56, 23, 105, 12, 89]))
