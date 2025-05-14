set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

set1.add(6)
print(f"set after adding 6: {set1}")

set1.remove(2)
print(f"set after removing 2: {set1}")

set1.discard(10)
print(f"set after discarding 10: {set1}")

union_set = set1.union(set2)
print(f"Union of {set1} and {set2}: {union_set}")

intersection_set = set1.intersection(set2)
print(f"Intersection of {set1} and {set2}: {intersection_set}")

difference_set = set1.difference(set2)
print(f"Difference of {set1} and {set2}: {difference_set}")

super_set = union_set.issuperset(set2)
print(f"Is {union_set} a superset of {set2}? {super_set}")

sub_set = set2.issubset(union_set)
print(f"Is {set2} a subset of {union_set}? {sub_set}")

set1.clear()
print(f"set1 after clearing: {set1}")