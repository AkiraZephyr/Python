def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def divide(a, b):
    return a/b
def multiply(a, b):
    return a*b
print("Enter 2 numbers to perform mathematical operations")
num1 = int(input("First Number"))
num2 = int(input("Second Number"))
print(f"Addition \t: {add(num1,num2)}")
print(f"Difference \t: {subtract(num1,num2)}")
print(f"Quotient \t: {divide(num1,num2)}")
print(f"Product \t: {multiply(num1,num2)}")