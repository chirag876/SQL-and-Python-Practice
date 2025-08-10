# In this order is not preserved
mylist = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
result = list(set(mylist))  # Remove duplicates by converting to a set
print("List after removing duplicates:", result)

# In this order is preserved
mylist2 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
result2 = []
for item in mylist2:
    if item not in result2:
        result2.append(item)  # Append only unique items
print("List after removing duplicates while preserving order:", result2)
