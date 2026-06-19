'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.'''


def uniquestringchar(s):  # not an optimized solution
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1


s = "lleettccooddemm"
print(uniquestringchar(s))


class Solution(object):
    def firstUniqChar(self, s):  # optimized solution
        """
        :type s: str
        :rtype: int
        """
        s1 = {}
        for i in s:
            if i in s1:
                s1[i] += 1
            else:
                s1[i] = 1
        for idx, ch in enumerate(s):
            if s1[ch] == 1:
                return idx
        return -1
