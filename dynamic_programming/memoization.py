"""
Memoization is an optimization technique used to speed up programs
by storing the results of expensive function calls
and returning the cached result when the same inputs occur again.

It can be realized using function closure in Python (and decorators)

In Python there's a module named functools with a method lru_cache()
which allows us to use this optimization technique

First, we'll implement memoization on our own with an example function, then with the help of lru_cache
"""
from functools import wraps
from functools import lru_cache

# 1
# Memoize using external dictionary for storing values
cache = {}


def memoized_add_to_80(n):
    if n in cache:
        return cache[n]
    else:
        print("long time")
        cache[n] = n + 80
        return cache[n]


# 2
# Memoize using decorators and function closure
def memoize(fn):
    memo = {}

    @wraps(fn)
    def helper(x):
        if x not in memo:
            print("long time")
            memo[x] = fn(x)
        return memo[x]

    return helper


@memoize
def add_to_80(n):
    return n + 80


# 3
# using method lru_cache() from module functools
@lru_cache(maxsize=1000)
def lru_add_to_80(n):
    return n + 80


if __name__ == "__main__":
    # Memoize using external dictionary for storing values
    print('1', memoized_add_to_80(5))
    print('2', memoized_add_to_80(5))
    print('3', memoized_add_to_80(6))
    print()
    # Memoize using decorators and function closure
    print('1', add_to_80(5))
    print('2', add_to_80(5))
    print('3', add_to_80(6))
    print()
    # Memoize using lru_cache()
    print('1', lru_add_to_80(5))
    print('2', lru_add_to_80(5))
    print('3', lru_add_to_80(6))
    print('3', lru_add_to_80(6))
    print('3', lru_add_to_80(6))
    print('3', lru_add_to_80(6))
    print('3', lru_add_to_80(2))
    print(lru_add_to_80.cache_info())
