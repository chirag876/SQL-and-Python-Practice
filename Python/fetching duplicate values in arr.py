"""Problem Statement: Write a Python program to fetch duplicate values in an array.
Input: [1,2,3,4,5,6,8,8,6,6,5,5,8,8,6,5]
Output: [5, 6, 8]"""


def fetch_duplicate_values(arr):
    seen = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
                if arr[i] == arr[j] and arr[i] not in seen: 
                        seen.append(arr[i])
    return seen
arr1 = [1,2,3,4,5,6,8,8,6,6,5,5,8,8,6,5]

print(fetch_duplicate_values(arr1))