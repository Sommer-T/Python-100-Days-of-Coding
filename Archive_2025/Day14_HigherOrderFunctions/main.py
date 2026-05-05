# Day 14 - Higher Order Functions & Scope

def greet():
    return "Hello!"

def call_function(func):
    print("Calling the function passed in:")
    print(func())  # Call the function

call_function(greet)

# ------------------------------

# Nested functions and scope example

def outer_function():
    message = "Inner function can access this."

    def inner_function():
        print(message)

    inner_function()

outer_function()

# ------------------------------

# Example: Higher-order math function

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def math_operation(a, b, operation):
    return operation(a, b)

print(math_operation(10, 5, add))
print(math_operation(10, 5, subtract))