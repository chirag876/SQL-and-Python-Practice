'''Given a string s, the task is to create a dictionary where each key is a character present in the string and the corresponding value is a list of all indices at which that character occurs in the string.

Input:  s = "aabcbdc"
Output: {'a': [0, 1], 'b': [2, 4], 'c': [3, 6], 'd': [5]}
'''

# ------------------------------------------- Using logic--------------------------------------------------------------
from collections import defaultdict


def mappingvalueindex(strs):

    charposition = {}

    for index, value in enumerate(strs):

        if value not in charposition:
            charposition[value] = []

        charposition[value].append(index)
    return charposition


s = "aabcbdc"
print("Mapping of index and value:", mappingvalueindex(s))

# ================================================= Using in built method


def mappingindexvalue2(st):

    charpos = defaultdict(list)

    for index, value in enumerate(st):
        charpos[value].append(index)
    return dict(charpos)


s = "aabcbdc"
print("Mapping of index and value using defaultdict:", mappingvalueindex(s))
