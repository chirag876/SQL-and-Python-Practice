'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]'''

nums1 = [1,2,2,1]
nums2 = [2,2]

res1=set(nums1)
res2=set(nums2)
res3=res1.intersection(res2)
print("Intersection of array:", list(res3))