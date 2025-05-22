import copy
original_list = [1, 2, [3, 4]]
shallow_copy_list = copy.copy(original_list)
deep_copy_list = copy.deepcopy(original_list)
shallow_copy_list[2][0] = 5
shallow_copy_list[0] = 10
print("Original List:", original_list)
print("Shallow Copy List:", shallow_copy_list)
print("Deep Copy List:", deep_copy_list)