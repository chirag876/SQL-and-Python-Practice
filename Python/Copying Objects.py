# ------------------------------------------------- Shallow Copy Example ---------------------------------
import copy

# Create a list with some sample data
original_list = [1, 2, 3, [4, 5]]
# Create a shallow copy of the list
copied_list = copy.copy(original_list)
# Modify the original list
original_list[3][0] = 2  # This will affect the shallow copy as well
# Print both lists to see the effect of the shallow copy
print("Original list:", original_list)
print("Shallow copied list:", copied_list)


# --------------------------------- Deep Copy Example ---------------------------------
original_list2 = [1, 2, 3, [4, 5]]
# Create a deep copy of the list
deep_copied_list = copy.deepcopy(original_list2)
# Modify the original list again
original_list2[3][1] = 3  # This will not affect the deep copy
# Print both lists to see the effect of the deep copy
print("Original list 2:", original_list2)
print("Deep copied list:", deep_copied_list)
