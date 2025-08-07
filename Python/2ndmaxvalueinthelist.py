def second_max_value(lst):
    unique= list(set(lst))  # Remove duplicates by converting to a set
    print("Unique values in the list:", unique)
    unique.sort(reverse= True)  # Sort the list in ascending order
    print("Sorted unique values in descending order:", unique)
    if len(unique) <2:
        return None
    return unique[1]  # Return the second maximum value

# Example usage
lst = [1, 3, 2, 8, 5, 5, 6,9, 4, 7, 10]
result = second_max_value(lst)
print("The second maximum value in the list is:", result)
    