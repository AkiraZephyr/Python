from collections import deque
nums = deque([1,2,3,4,5])
print(f"Before Rotation{list(nums)}")
nums.rotate(1)
print(f"Rotation with 1")
print(list(nums))
print(f"Rotation with -1")
nums.rotate(-1)
print(list(nums))