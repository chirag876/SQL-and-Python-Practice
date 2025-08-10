'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2'''

def subarraysum(lst, targetsum):
    count=0
    
    # outer loop for starting point of subarray
    for i in range(len(lst)):
        currentsum = 0 # reset sum of each starting point
        for j in range(i, len(lst)): # inner loop to extend subarray from start
            currentsum+=lst[j] # add the current sum to element
            if currentsum==targetsum:
                count+=1 # found a valid subarray
    return count
    
nums = [1,2,3]
k = 3
print("total number of subarrays whose sum equals to k:", subarraysum(nums,k))