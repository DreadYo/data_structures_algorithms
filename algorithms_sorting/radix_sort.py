"""
Time complexity     -   O(n * k)
Space complexity    -   O(n + k)
"""


def radix_sort(array, rang):
    # max count of rank
    length = len(str(max(array)))
    for i in range(length):
        temp = [[] for k in range(rang)]  # list of length of rang, consists of empty lists
        for x in array:
            figure = x // 10 ** i % 10
            temp[figure].append(x)
        array = []
        for k in range(rang):
            array = array + temp[k]
    return array


if __name__ == "__main__":
    numbers = [2, 8, 1, 4, 14, 7, 16, 10, 9, 3]
    print(numbers)
    print(radix_sort(numbers, 10))

