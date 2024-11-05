def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def clear()
    return True



print("Please enter the operation to perform:")
print("1 - ADDITION")
print("2 - SUBTRACTION")
print("3 - MULTIPLICATION")
print("4 - DIVISION")

operation = input("\n")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if operation == "1":
    print("The result is:", add(a, b))
elif operation == "2":
    print("The result is:", subtract(a, b))
elif operation == "3":
    print("The result is:", multiply(a, b))
elif operation == "4":
    print("The result is:", divide(a, b))
else:
    print("Please enter a valid operation")
