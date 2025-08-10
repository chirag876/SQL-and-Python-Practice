'''Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.'''

def maxsum(lst):
    maxsum = lst[0]
    currentsum = 0
    start = 0
    temp = 0 # temp start value
    end = 0
    for i, num in enumerate(lst):
        currentsum+=num
        if currentsum>maxsum:
            maxsum = currentsum
            start = temp
            end = i
        elif currentsum < 0:
            currentsum = 0
            temp = i+1 # next sub array will start from here
    return maxsum, lst[start:end+1]

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxsumvalue, subarray = maxsum(nums)
print("Max sum:", maxsumvalue)
print("sub array with the max sum:", subarray)
