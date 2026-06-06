"""**Problem Statement:**

Given a string, reverse only the vowels (a, e, i, o, u — both uppercase and lowercase) in it. All consonants stay at their original positions.

---

**Approach:**

1. Convert string to list — strings are immutable in Python
2. Two pointers — `left=0`, `right=len-1`
3. Loop while `left < right`:
   - `left` is on a consonant — move left forward
   - `right` is on a consonant — move right backward
   - Both on vowels — swap, move both inward
4. Join list back to string and return

---

Time complexity: O(n) — single pass."""

def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return ''.join(s_list)