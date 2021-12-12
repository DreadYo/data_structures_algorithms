"""
Time complexity     -   O(n + k)
Space complexity    -   O(k)
"""


def simple_counting_sort(array):
    scope = max(array) + 1
    temp = [0] * scope
    for x in array:
        temp[x] += 1
    array[:] = []
    for number in range(scope):
        array += [number] * temp[number]


if __name__ == "__main__":
    numbers = [2, 8, 1, 4, 14, 7, 16, 10, 9, 3]
    print(numbers)
    simple_counting_sort(numbers)
    print(numbers)
