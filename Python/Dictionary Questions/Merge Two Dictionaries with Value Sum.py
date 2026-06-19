'''Given two dictionaries, merge them into one. If a key exists in both dictionaries, sum their values.
Input: 

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

Output:

{'a': 400, 'b': 400, 'c': 300, 'd': 400}
'''


def mergedictionary(dict1, dict2):
    dict3 = dict1.copy()  # Create a copy of the first dictionary

    for key1, value1 in dict2.items():
        if key1 in dict3:
            dict3[key1] += value1 # If the key exists in both dictionaries, sum their values
        else:
            dict3[key1] = value1 # If the key does not exist in the first dictionary, add it to the merged dictionary

    return dict3


dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
print("Merged dictionary using loops:", mergedictionary(dict1, dict2))


# --------------------------------- Using collection and counter

from collections import Counter

def merged_dictionary_with_counter(dict1, dict2):
    mergeddictionary = dict(Counter(dict1) + Counter(dict2)) # Create a merged dictionary by summing the values of common keys using Counter
    return mergeddictionary


dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
print("Merged dictionary with counter method:", merged_dictionary_with_counter(dict1, dict2))
