import random

low = 1
high = 100
secret_number = random.randint(low, high)

print(f"Guess the number between {low} and {high}")

while True:
    guess = int(input("Your guess: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Congradulation! You got it!")
        break