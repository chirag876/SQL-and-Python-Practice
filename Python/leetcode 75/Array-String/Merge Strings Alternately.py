"""

**Merge Strings Alternately**

Given two strings `word1` and `word2`, merge them alternately. Add characters from `word1` first, then `word2`, one by one. If one string is longer than the other, append the remaining characters to the end.

**Example:**
```
word1 = "abc", word2 = "pqr" → "apbqcr"
word1 = "ab", word2 = "pqrs" → "apbqrs"
word1 = "abcd", word2 = "pq" → "apbqcd"
```
"""
def merge_alternately(word1, word2):
    result = ""
    for i in range (min(len(word1), len(word2))):
        result += word1[i]
        result += word2[i]
    if len(word1) > len(word2):
        result += word1[i+1:]
    result += word2[i+1:]
    return result

"""Approach: Two Pointers, checked the length of the strings and added the remaining characters to the result string. Time complexity is O(n) where n is the length of the longer string."""
