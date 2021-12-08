"""
Write 2 functions that finds the factorial of any number.
One should use recursive, the other should just use a for loop.

Recursive Rules:
1. Identify the base case
2. Identify the recursive case
3. Get closer and closer and return when needed. Usually you have 2 returns
"""


def find_factorial_recursive(number):
    # O(n) - Time complexity
    if number == 1:
        return 1
    return number * find_factorial_recursive(number - 1)


def find_factorial_iterative(number):
    # O(n) - Time complexity
    res = 1
    for i in range(1, number+1):
        res *= i
    return res


if __name__ == "__main__":
    print(find_factorial_recursive(10))
    print(find_factorial_iterative(10))
