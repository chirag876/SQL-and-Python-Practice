# Right rotation
lst = [1, 2, 3, 4, 5]
k = 2
k2 = k % len(lst)  # normalise k so that it is never greater then original list
res = lst[-k2:]+lst[:-k2]
print("Right rotation of list")
print(res, "\n")


# Left rotation
lst = [1, 2, 3, 4, 5]
k = 2
k2 = k % len(lst)  # normalise k so that it is never greater then original list
res = lst[k2:]+lst[:k2]
print("Left rotation of list")
print(res)
