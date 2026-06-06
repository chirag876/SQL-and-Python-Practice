"""**Problem Statement:**

You have a `flowerbed` array of `0s` and `1s` — `0` means empty, `1` means flower already planted. You cannot plant two flowers in adjacent slots. Given `n`, check if you can plant exactly `n` more flowers without violating the rule. Return `True` or `False`.

---

**Approach:**

1. Loop through every slot
2. For each slot check 3 conditions:
   - Current slot is empty: `flowerbed[i] == 0`
   - Left neighbor is empty or doesn't exist: `i == 0` or `flowerbed[i-1] == 0`
   - Right neighbor is empty or doesn't exist: `i == len(flowerbed)-1` or `flowerbed[i+1] == 0`
3. If all 3 true — place flower, mark `flowerbed[i] = 1`, increment count
4. If `count >= n` at any point — return `True`
5. Loop ends, still `count < n` — return `False`

---

Time complexity: O(n) — single pass."""

def can_place_flowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        l = (i == 0) or (flowerbed[i - 1] == 0)
        r = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
        if l and r and flowerbed[i] == 0:
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True
    return False
