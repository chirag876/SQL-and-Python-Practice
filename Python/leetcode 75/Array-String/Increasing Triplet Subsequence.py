"""**Problem — Increasing Triplet Subsequence:**
Given array `nums`, return `True` if there exist indices `i < j < k` such that `nums[i] < nums[j] < nums[k]`.

```
Input:  [2, 1, 5, 0, 4, 6]
Output: True  (1 < 4 < 6)

Input:  [5, 4, 3, 2, 1]
Output: False
```

**Approach — Two Variables O(N):**

1. Maintain two variables `first` and `second`, both initialized to infinity
2. Traverse array:
   - If current number ≤ `first` → update `first` (naya sabse chota mila)
   - Elif current number ≤ `second` → update `second` (naya doosra chota mila)
   - Else → teesra number mil gaya jo dono se bada hai → `True`
3. If loop ends without finding triplet → `False`

```
nums = [2, 1, 5, 0, 4, 6]

first=inf, second=inf
2 → first=2
1 → first=1
5 → second=5
0 → first=0
4 → second=4
6 → True ✓
```"""

def increasing_triplet(nums):
    first = second = float('inf') # first: smallest so far, second: second smallest so far
# start with infinity so any real number will be smaller handles negatives too
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False