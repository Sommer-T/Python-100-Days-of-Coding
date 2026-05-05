# Day 13 - Debugging Exercises

# 🛠 FizzBuzz (fixed version)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Debugging Example: Sum of even numbers

def sum_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

print("Sum of even numbers from 1 to 10:", sum_even(10))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2024))  # True