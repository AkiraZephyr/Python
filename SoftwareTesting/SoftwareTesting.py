#Simple Python program to demonstrate debugging a simple erorrs in the code

#This program is to find the sum of two numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum
print("Enter two numbers to add")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The sum of {num1} and {num2}: {add_numbers(num1, num2)}")