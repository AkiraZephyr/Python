fruits = ("Apple", "Banana", "Cherry", "Orange")
print ("Fruits Tuple", fruits)

print("First Fruit:", fruits[0])
print("Lasr Fruit:", fruits[-1])

print("First two fruits:", fruits[:2])

print ("Number of fruits:", len(fruits))

person = ("Alice", 25, "New York")
name, age, city = person
print ("Name : ", name)
print ("Age : ", age)
print ("City : ", city)

nested_tuple = (1, (2,3), (4,5,6))
print ("Nested Tuple : ", nested_tuple)
print ("Accessing Nest Tuple: ", nested_tuple[1][1])

numbers = (1,2,2,3,4,2,5)
print ("Count of 2 : ", numbers.count(2))

print("Index of Cherry:", fruits.index("Cherry"))
