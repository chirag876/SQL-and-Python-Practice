"""**Problem:**
Given array `nums`, move all `0`s to end while maintaining relative order of non-zero elements. Must do in-place.

```
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

**Approach — Two Pointer:**

1. `left` pointer track karta hai — next non-zero element kahan place karna hai
2. `right` pointer traverse karta hai poora array
3. Jab `right` pe non-zero mile → `left` pe place karo, `left` aage badhao
4. Loop ke baad `left` se end tak sab `0` fill karo

```
nums = [0, 1, 0, 3, 12]
left = 0

right=0 → 0 hai, skip
right=1 → 1 hai, nums[left]=1, left=1
right=2 → 0 hai, skip
right=3 → 3 hai, nums[left]=3, left=2
right=4 → 12 hai, nums[left]=12, left=3

left se end tak 0 fill → [1, 3, 12, 0, 0]
```"""

from ast import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            l =0
            for r in range(len(nums)):
                if nums[r]:
                    nums[l], nums[r] =  nums[r], nums[l]
                    l +=1
            return nums
        