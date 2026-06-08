"""**Problem:**
Given a string `s`, reverse the order of words. Words are separated by spaces. Return the result with single spaces, no leading/trailing spaces.

```
Input:  "  the sky   is blue  "
Output: "blue is sky the"
```

**Approach:**
1. Strip leading/trailing spaces and split string into words — handle multiple spaces automatically
2. Reverse the list of words
3. Join them back with single space and return

Edge cases to consider:
- Multiple spaces between words
- Leading/trailing spaces
- Single word string"""

def reverse_words(s):
    return " ".join(reversed(s.strip().split()))


def reverse_words2(s):
    return " ".join(s.split()[::-1])