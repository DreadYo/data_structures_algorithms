"""
53. Maximum Subarray (Leetcode)

Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# The first solution that I comes to mind, as always, it's the brute force solution
from typing import List


def max_sub_array_bruteforce(nums: List[int]) -> int:
    maximum = 0
    if len(nums) == 0:
        return None
    for i in range(len(nums)):
        sub_sum = 0
        for j in range(i, len(nums)):
            sub_sum += nums[j]
            maximum = max(maximum, sub_sum)
    return maximum

# Time complexity - O(n^2)

# Faster solution.
# Loop over the array and for every iteration check for the maximum subarray ending at that index.
# It's possible 2 situations:
# - sum of the maximum subarray ending at the previous index plus current element.
# - current element only


def max_sub_array(nums: List[int]) -> int:
    if len(nums) == 0:
        return None
    maximum = maxsub = nums[0]
    for i in range(1, len(nums)):
        maxsub = max(maxsub + nums[i], nums[i])
        maximum = max(maximum, maxsub)
    return maximum

# We set the variables maximum and maxarray to the value of the first element of the array.
# Then we loop over the entire array from the first index.
# At every iteration, we update the value of maxarray to be the maximum among the current element
# and the sum of the maxarray ending at the previous index and the current element
# This way, maxarray stores the maximum subarray ending at index i
# And the variable maximum stores the maximum among all the maxarrays ending at every index,
# effectively storing the global maximum
# Since this requires only one for loop, the time complexity is an efficient O(n)!

print(max_sub_array_bruteforce([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_array_bruteforce([1]))
print(max_sub_array_bruteforce([5,4,-1,7,8]))

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_array([1]))
print(max_sub_array([5,4,-1,7,8]))