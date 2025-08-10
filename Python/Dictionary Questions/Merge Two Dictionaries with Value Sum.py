'''Given two dictionaries, merge them into one. If a key exists in both dictionaries, sum their values.
Input: 

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

Output:

{'a': 400, 'b': 400, 'c': 300, 'd': 400}
'''
from collections import Counter


def mergedictionary(dict1, dict2):
    dict3 = dict1.copy()

    for key1, value1 in dict2.items():
        if key1 in dict3:
            dict3[key1] += value1
        else:
            dict3[key1] = value1

    return dict3


dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
print("Merged dictionary using loops:", mergedictionary(dict1, dict2))


# --------------------------------- Using collection and counter


def mergeddictionarywithcounter(dict1, dict2):
    mergeddictionary = dict(Counter(dict1) + Counter(dict2))
    return mergeddictionary


dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
print("Merged dictionary with counter method:", mergedictionary(dict1, dict2))
