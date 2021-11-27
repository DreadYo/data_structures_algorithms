"""
217. Contains Duplicate (Leetcode)

Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

# The first solution that comes to mind, as always, it's brute force solution
# I go through array and count how many times every value is appear.
# I use nested loop.
# Than complexity will O(n^2)


def contains_duplicate_brute(nums) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


print(contains_duplicate_brute([1,2,3,1]))
print(contains_duplicate_brute([1,2,3,4]))
print(contains_duplicate_brute([1,1,1,3,3,4,3,2,4,2]))

# Than I try to solve this problem using hash table (dictionary).

def contains_duplicate(nums) -> bool:
    # create dictionary
    dictionary = dict()
    # go through array
    for el in nums:
        # if element doesn't exist in dictionary
        if el not in dictionary:
            # put element in dictionary
            dictionary[el] = True
        else:
            # than element exists
            return True
    return False


print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))

# Time complexity of this solution - O(n)
# Space complexity - O(n)
