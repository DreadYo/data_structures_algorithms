"""
House Robber (Leetcode 198)
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is
that adjacent houses have security systems connected and
it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from functools import wraps
from functools import lru_cache


# 1. Brute-force solution.
# 2 choices for each house:
# - don't rob and move to next
# - rob and move to the house after next
# Time complexity - O(2^n).
# Where n is the number of elements in A.
# At each index, we have two choices of either robbing or not robbing the current house.
# Space complexity - O(n).
# required by implicit recursive stack. The max depth of recursion can go upto n.
def brute_force_robber(nums, index=0):
    if index >= len(nums):
        return 0
    return max(brute_force_robber(nums, index+1), nums[index] + brute_force_robber(nums, index+2))


# 2. Dynamic programming. With creating closure
# Time complexity - O(n).
# We calculate the result for each index only once and
# there are n indices.
# Space complexity - O(n).
def dynamic_robber_massive(nums):
    def memoize(fn):
        memo = {}

        @wraps(fn)
        def helper(nums, index=0):
            if index not in memo:
                print("long time")
                memo[index] = fn(nums, index)
            return memo[index]

        return helper

    @memoize
    def dynamic_robber(nums, index=0):
        if index >= len(nums):
            return 0
        return max(dynamic_robber(nums, index + 1), nums[index] + dynamic_robber(nums, index + 2))

    return dynamic_robber(nums)


# 3. Dynamic programming using @lru_cache()
def dynamic_robber_nice(nums):
    @lru_cache(maxsize=1000)
    def rob(index):
        if index >= len(nums):
            return 0
        return max(rob(index+1), nums[index] + rob(index+2))
    return rob(0)


if __name__ == "__main__":
    # brute-force
    num1 = [1, 2, 3, 1]
    print(brute_force_robber(num1))
    num2 = [2, 7, 9, 3, 1]
    print(brute_force_robber(num2))
    print()
    # dynamic programming
    num1 = [1, 2, 3, 1]
    print(dynamic_robber_massive(num1))
    num2 = [2, 7, 9, 3, 1]
    print(dynamic_robber_massive(num2))
    print()
    # dynamic programming (lru_cache)
    num1 = [1, 2, 3, 1]
    print(dynamic_robber_nice(num1))
    num2 = [2, 7, 9, 3, 1]
    print(dynamic_robber_nice(num2))
    print()



