import math

x = float(input("Enter a number (x) : "))
y = float(input("Enter another number (y) : "))
print("\n---Built-in Functions---")
print(f"Absolute value of x : {abs(x)}")
print(f"{x} raised to the power {y} : {pow(x,y)}")
print(f"Minimum of {x} and {y} : {min(x,y)}")
print(f"Maximum of {x} and {y} : {max(x,y)}")
print(f"Round {x} to 2 decimal places : {round(x,2)}")
print("\n---Math Module Functions---")
print(f"Square root of {x} : {math.sqrt(abs(x))}")
print(f"Ceiling of {x} : {math.ceil(x)}")
print(f"Floor of {x} : {math.floor(x)}")

if x >= 0 and x.is_integer():
    print(f"Factorial of int {x} : {math.factorial(int(x))}")
else:
    print("Factorial: not defined for negative or non-integer x")

if x > 0:
    print(f"Natural log of {x} : {math.log(x)}")
    print(f"Log base of 10 of {x} : {math.log10(x)}")
    print(f"e raised to power {x} : {math.exp(x)}")
else:
    print("Logs: not defined for non-positive x")
print("\n---Trigonometric Functions(in radians)---")
print(f"Sine of {x} : {math.sin(x)}")
print(f"Cosine of {x} : {math.cos(x)}")
print(f"Tangent of {x} : {math.tan(x)}")

print("\n---Constants---")
print(f"Value of pi : {math.pi}")