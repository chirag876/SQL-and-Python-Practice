'''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]'''

s = ["h", "e", "l", "l", "o"]
print(s[::-1])

'''The above solution is not a feasible one because this will create a new list which will take extra space, the above method can be useful in case of string litral as they are immutable so we have to create a new one'''


# ----------------------- Two pointer approach to save the memory

s2 = ["C", "H", "I", "R", "A", "G"]

left, right = 0, len(s2) - 1
while left < right:
    s2[left], s2[right] = s2[right], s2[left]
    left += 1
    right -= 1
print(s2)


s2 = 'Chirag'

left, right = 0, len(s2) - 1
while left < right:
    s2[left], s2[right] = s2[right], s2[left]
    left += 1
    right -= 1
print(s2)
