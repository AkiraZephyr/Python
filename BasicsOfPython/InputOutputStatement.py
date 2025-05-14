name = input("Enter your name:")
print(f"Hello {name}!")

age = int(input("\nEnter your age:"))
print(f"You will be {age + 5} in 5 years.")

price = float(input("\nEnter the price:"))
print(f"Price : {price}")
print(f"Price with tax: {price * 1.25}")

name, age = input("\nEnter your name and age:").split()
print(f"Name : {name}, Age : {age}")

a,b,c = map(int, input("\nEnter 3 numbers:").split())
print(f"Sum of 3 numbers: {a+b+c}")