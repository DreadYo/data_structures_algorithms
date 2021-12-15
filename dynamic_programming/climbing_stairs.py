"""
70. Climbing Stairs (Leetcode 70)
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

"""
Let's consider how different ways depend on the number of stairs.
n = 1
1. 1

n = 2
1. 1 + 1
2. 2

n = 3
1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1

n = 4
1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 2 + 1
4. 2 + 1 + 1
5. 2 + 2

n = 5
1. 1 + 1 + 1 + 1 + 1
2. 1 + 1 + 1 + 2
3. 1 + 1 + 2 + 1
4. 1 + 2 + 1 + 1
5. 1 + 2 + 2
6. 2 + 1 + 1 + 1
7. 2 + 1 + 2
8. 2 + 2 + 1

At ith step all different ways consist of:
1) 1 + all different ways from (i-1)th step and
2) 2 + all different ways from (i-2)th step. 

It looks like very similar to Fibonacci numbers.

"""
from functools import lru_cache


# brute-force solution
def climb_stairs(n):
    # print("call recursion")
    if n <= 2:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)


# solution using dynamic programming
@lru_cache(maxsize=50)
def climb_stairs_dynamic(n):
    # print("call recursion")
    if n <= 2:
        return n
    return climb_stairs_dynamic(n-1) + climb_stairs_dynamic(n-2)


if __name__ == "__main__":
    print("brute force")
    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(4))
    print(climb_stairs(10))
    print("dynamic")
    # print(climb_stairs_dynamic(4))
    print(climb_stairs_dynamic(50))
    print(climb_stairs_dynamic.cache_info())

