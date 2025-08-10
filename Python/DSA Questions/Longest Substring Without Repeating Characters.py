'''Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''

def substringwithmaxlength(str1):
   longestlenght = 0 # Will store the length of the longest substring found
   # Outer loop: Start checking from each character in the string
   for i in range(len(str1)): 
       sub= "" # current substring without duplicate characters
       # Inner loop: Extend the substring starting from index i
       for j in range(i, len(str1)):
           if str1[j] in sub: # If the current character is already in 'sub', we found a duplicate → stop this loop
               break
           sub +=str1[j] # If no duplicate, add the current character to 'sub'
       longestlenght = max(longestlenght, len(sub)) # Update the longest length if the current substring is longer
   return longestlenght
       
str1 = 'pwk'
print(substringwithmaxlength(str1))