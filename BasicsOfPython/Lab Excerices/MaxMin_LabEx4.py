numbers = [5,2,4,10,-1,8,1,9]
numbers.sort()
print(numbers)
min_value = numbers[0]
max_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num

print(f"Minimum value : {min_value}")

for num in numbers:
    if num > max_value:
        max_value = num

print(f"Maximum Value : {max_value}")