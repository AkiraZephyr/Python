print("Enter 2 numbers")
num1 = input()
num2 = input()
#num2 = input("Enter a number")
if num1 > num2:
    print("The number", num1, "is greater than ", num2)
elif num2 > num1:
    print("The number", num2, "is greater than ", num1)
else:
    print("Both numbers are equal")