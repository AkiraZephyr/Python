def swap_values(a, b):
    return b, a

print("Enter two values:")
a = input("Value 1: ")
b = input("Value 2: ")
print(f"Before swapping: a = {a}, b = {b}")
a, b = swap_values(a, b)
print(f"After swapping: a = {a}, b = {b}")