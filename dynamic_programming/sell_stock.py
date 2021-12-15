"""
Best Time to Buy and Sell Stock (Leetcode 121)

You are given an array prices
where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day
to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""
from functools import lru_cache


# The most common and easy solution is a brute force solution.
# But it's too inefficient solution.
# Time complexity - O(n^2)
# Space complexity - O(1)
def brute_force_profit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit


# Classical dynamic programming problem.
# Let dp[i] be a maximum profit we can have if we sell stock at i-th moment of time.
# Then we can get, that dp[i+1] = max(dp[i] + q, q), where q = nums[i+1] - nums[i],
# we have two choices, either we just buy and immeditely sell and get q gain,
# or we use dp[i] + q to merge two transactions.
# Note now, that we do not really need to keep all dp array, but we can keep only last state.
# Complexity: time complexity is O(n), space complexity is O(1).
def max_profit(prices):
    dp = 0
    ans = 0

    for i in range(len(prices)-1):
        q = prices[i+1] - prices[i]
        dp = max(dp + q, q)
        ans = max(ans, dp)
    return ans


if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]
    print(brute_force_profit(prices1))
    prices2 = [7, 6, 4, 3, 1]
    print(brute_force_profit(prices2))
    print()
    prices1 = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices1))
    prices2 = [7, 6, 4, 3, 1]
    print(max_profit(prices2))
