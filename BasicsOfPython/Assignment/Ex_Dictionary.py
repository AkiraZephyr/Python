old_list=[1,2,3,4,5]
squares = [x**2 for x in old_list]
evens = [x for x in squares if x % 2 == 0]
print(old_list)
print(squares)
print(evens)


nums = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, nums))
print(nums)

nums = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)

from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)

words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)

names = ["Alice", "Bob"]
ages = [25, 30]
combined = list(zip(names, ages))
print(combined)

import itertools

nums = [1, 2, 3]
perms = list(itertools.permutations(nums))
comb = list(itertools.combinations(nums, 2))
print(perms)
print(comb)

names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names if len(name) > 3]
print(capitalized)