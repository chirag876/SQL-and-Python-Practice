'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true'''

# s = "anagram"
# t = "nagaram"


def anagramcheck(s, t):
    if len(s) != len(t):  # if length differ they can't be anagrams
        return False

    if sorted(s) == sorted(t):  # convert both string into sorted list of characters
        return True
    return False


s = "anagram"
t = "nagaram"
print(anagramcheck(s, t))
