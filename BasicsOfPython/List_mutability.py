fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange" 
print(fruits)

fruits.append("grape")
print(fruits)
fruits.insert(1, "kiwi")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.pop(2)
print(fruits)
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30]
print(numbers)