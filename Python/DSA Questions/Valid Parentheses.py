'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false'''


def validparenthesis(strs):
    bracketmap = {'}': '{', ']': '[', '(': ')'}
    emstc = []

    for char in strs:
        if char in bracketmap.values():  # if it is an opening bracket
            emstc.append(char)

        elif char in bracketmap:

            # if stack is empty or top of the stack is not matching the opening bracket then invalid
            if not emstc and emstc[-1] != bracketmap[char]:

                return False
            emstc.pop()  # pop the matched opening bracket
        else:
            return False  # invalid character not a bracket
    # if the stack is empty all the brackets is matched correctly
    return len(emstc) == 0


strs = '{[]}'
print("Valid Parenthesis:", validparenthesis(strs))
