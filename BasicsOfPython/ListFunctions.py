numbers = [10,20,30,40,50]
print(f"Before List Functions : {numbers}")

print("\nAppend() Function")
numbers.append(60)
print(f"After Append : {numbers}")

print("\nExtend() Function")
numbers.extend([70,80,90])
print(f"After Extend : {numbers}")

print("\nInsert() Function")
numbers.insert(2,25)
print(f"After Insert : {numbers}")

print("\nRemove() Function")
numbers.remove(30)
print(f"After Remove : {numbers}")

print("\nPop() Function")
popped_element = numbers.pop()
print(f"Popped Element : {popped_element}")
print(f"After Pop : {numbers}")

print("\nIndex() Function")
index = numbers.index(40)
print(f"Index of 40 : {index}")

print("\nCount() Function")
count = numbers.count(20)
print(f"Count of 20 : {count}")

print("\nSort() Function")
print(f"Before Sort : {numbers}")
numbers.sort()
print(f"After Sort : {numbers}")

print("\nReverse() Function")
print(f"Before Reverse : {numbers}")
numbers.reverse()
print(f"After Reverse : {numbers}")

print("\nCopy() Function")
new_list = numbers.copy()
print(f"Copied List : {new_list}")

print("\nClear() Function")
numbers.clear()
print(f"After Clearing : {numbers}")
print(f"New List : {new_list}")