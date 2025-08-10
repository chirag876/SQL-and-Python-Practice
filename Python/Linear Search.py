def linear_search(arr, target):
    """ Perform a linear search for target in arr.
    Returns the index of target if found, otherwise returns -1."""
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


arr1 = [1, 2, 3, 4, 5]
target1 = 1
result1 = linear_search(arr1, target1)
if result1 != -1:
    print(f"Element {target1} found at index {result1}.")
else:
    print(f"Element {target1} not found in the array.")
