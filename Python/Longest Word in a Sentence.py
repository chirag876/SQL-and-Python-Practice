'''Given a sentence S, write a program to find the longest word. If there are multiple words with the same length, return the first one.
Input:

S = "Python is an amazing programming language"

Output:

programming

'''

def longestwordcheck(strs):
    longestword = ""
    maxlength = 0
    strs2 = strs.split()
    
    for char in strs2:
        length = len(char)
        if length > maxlength:
            maxlength = length
            longestword = char
    return longestword

S = "Python is an amazing programming language"
print(longestwordcheck(S))