'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]'''


def groupanagrams(strs):
    lst2 = []
    for char in strs:
        placed = False
        for item in lst2:
            if sorted(char) == sorted(item[0]):
                item.append(char)
                placed = True
                break
        if not placed: # if no existing group match create a new one
            lst2.append([char])
    return lst2

strs = ["eat","tea","tan","ate","nat","bat"]
print("Group anagrams:", groupanagrams(strs))