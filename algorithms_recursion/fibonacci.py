"""
Given a number N return the index value of Fibonacci sequence,
where the sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

Recursive Rules:
1. Identify the base case
2. Identify the recursive case
3. Get closer and closer and return when needed. Usually you have 2 returns
"""


def fibonacci_iterative(n):
    # O(n) - Time complexity
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[-1]


def fibonacci_iterative_without_arr(n):
    # O(n) - Time complexity
    first_number = 0
    second_number = 1
    if n == 0:
        return first_number
    if n == 1:
        return second_number
    for i in range(2, n+1):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
    return third_number


def fibonacci_recursive(n):
    # O(2^n) - Time complexity  (2 to the power of n)
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == "__main__":
    print(fibonacci_iterative(8))
    print(fibonacci_iterative_without_arr(8))
    print(fibonacci_recursive(8))

