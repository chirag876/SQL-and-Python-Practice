'''Given a dictionary with unique values, write a program to create a new dictionary by swapping its keys and values.

Input: dict1 = {'a': 1, 'b': 2, 'c': 3}

Output: {1: 'a', 2: 'b', 3: 'c'}

'''


def swappingdictkeyvalue(dict):
    dict2 = {}

    for key, value in dict.items():
        dict2[value] = key
    return dict2


dict1 = {'a': 1, 'b': 2, 'c': 3}
print(swappingdictkeyvalue(dict1))
