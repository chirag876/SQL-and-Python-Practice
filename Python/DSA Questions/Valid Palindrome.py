'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.'''

s = "A man, a plan, a canal: Panama"
s2 = "".join(char.lower() for char in s if char.isalnum())
isvalidpalindrome = s2 == s2[::-1]
print(isvalidpalindrome)
