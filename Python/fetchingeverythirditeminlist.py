def fetchingthirditeminlist(lst):
    result = []
    for i in range(2, len(lst), 3):
        result.append(lst[i])
    return result


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("3 elemet:", fetchingthirditeminlist(lst1))


def fetchingthirditeminlist(lst):
    result = []
    for i in range(2, len(lst), 3):
        result.append(lst[i])
    return result


lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [lst2[i] for i in range(2, len(lst2), 3)]
print("3 elemet:", result)
