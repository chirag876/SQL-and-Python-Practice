"""## Problem Statement

**Given an array of elements, find the frequency of each element and return the result as a dictionary where:**

* Key = Element
* Value = Number of occurrences of that element

### Example

Input:

```python
[1,2,2,3,3,3]
```

Output:

```python
{
    1: 1,
    2: 2,
    3: 3
}
```

---

## Approach

### Step 1

Create an empty dictionary to store the frequency of each element.

```python
freq = {}
```

### Step 2

Traverse the array one element at a time.

```python
for item in arr:
```

### Step 3

Check whether the current element already exists in the dictionary.

* If it does not exist, initialize its count to `1`.
* If it already exists, increment its count by `1`.

### Step 4

Continue until all elements have been processed.

### Step 5

Return the frequency dictionary.

---

## Dry Run

Input:

```python
[1,2,2,3]
```

Iteration 1:

```python
{1: 1}
```

Iteration 2:

```python
{1: 1, 2: 1}
```

Iteration 3:

```python
{1: 1, 2: 2}
```

Iteration 4:

```python
{1: 1, 2: 2, 3: 1}
```

Final Output:

```python
{
    1: 1,
    2: 2,
    3: 1
}
```

---

## Time and Space Complexity

| Complexity Type  | Value |
| ---------------- | ----- |
| Time Complexity  | O(n)  |
| Space Complexity | O(k)  |

Where:

* `n` = total number of elements in the array
* `k` = number of unique elements

---

## Interview Explanation (30-Second Answer)

> "I used a dictionary to maintain a mapping between each element and its frequency. I traverse the array once, checking whether the current element already exists in the dictionary. If it does not exist, I initialize its count to 1; otherwise, I increment its existing count. This approach runs in O(n) time with O(k) extra space, where k is the number of unique elements."

"""

def freofvalue(arr):
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
        freq.update({i:freq[i]})
    return freq
arr1 = [1,2,3,4,5,6,8,8,6,6,5,5,8,8,6,5,6,7]

print(freofvalue(arr1))