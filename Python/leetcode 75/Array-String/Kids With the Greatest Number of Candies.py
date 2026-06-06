"""**Problem Statement:**

You have an array `candies[]` where each index represents a kid's candy count, and a number `extraCandies`. For each kid, check: if you give all `extraCandies` to that kid alone, will they have the greatest number of candies (greater than or equal to current max)? Return a boolean array.

---

**Approach:**

1. Find `max` of the array once — this is your fixed benchmark
2. Loop through every kid
3. Check if `candies[i] + extraCandies >= max`
4. Store `True/False` in result list
5. Return result list

Time complexity: O(n) — one pass for max, one pass for loop."""


def kids_with_candies(candies, extra_candies):
    list1 = []
    max_candies = max(candies)
    for i in range(len(candies)):
        list2 = candies[i] + extra_candies >=max_candies
        list1.append(list2)
    return list1
            