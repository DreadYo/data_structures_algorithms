"""
Now we will implement our old Fibonacci program using Dynamic Programming
Fibonacci Sequence : 0 1 1 2 3 5 8 13 21 35 55 89 144 233 . . .
"""
from functools import wraps
from functools import lru_cache


# 1. Old solution.
# Time complexity - O(2^n)
# Space complexity - O(n)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# 2. New solution using dynamic programming.
# Time complexity - O(n)
# Space complexity - O(n)
def memoize(fn):
    memo = {}

    @wraps(fn)
    def helper(x):
        if x not in memo:
            # print("long time")
            memo[x] = fn(x)
        return memo[x]

    return helper


@memoize
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n-1) + fibonacci2(n-2)


# 3. Using method lru_cache() from module functools.
# Time complexity - O(n)
# Space complexity - O(n)
@lru_cache(maxsize=1000)
def fibonacci3(n):
    if n < 2:
        return n
    return fibonacci3(n-1) + fibonacci3(n-2)


if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci2(100))
    print(fibonacci3(100))
    print(fibonacci3.cache_info())
