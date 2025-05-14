def is_even(n):
    return n % 2 == 0

n = int(input("Enter a number: "))
if is_even(n):
    print(f"{n} is even")
else:
    print(f"{n} is odd")