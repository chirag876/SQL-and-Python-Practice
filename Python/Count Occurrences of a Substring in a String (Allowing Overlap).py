'''
Given two strings string and sub_string, determine how many times sub_string appears in string.
Occurrences can overlap.

Input:
string = "ABCDCDC"
sub_string = "CDC"

Output:
2

Explanation:
"CDC" appears starting at index 2 and index 4.

'''


def substringoccurencecount(strs, substrs):
    count = 0
    for i in range(len(strs) - len(substrs)+1):
        if strs[i:i+len(substrs)] == substrs:
            count += 1
    return count


strs = 'ABCDCD'
substrs = 'CD'
print('Count of occurrence of substring in main string:',
      substringoccurencecount(strs, substrs))
