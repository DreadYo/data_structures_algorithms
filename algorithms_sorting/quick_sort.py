"""
Quick Sort
Quick Sort is another sorting algorithm which follows divide and conquer approach.
It requires to chose a pivot,
then place all elements smaller than the pivot on the left of the pivot
and all elements larger on the right
Then the array is partitioned in the pivot position and
the left and right arrays follow the same procedure until the base case is reached.
After each pass the pivot element occupies its correct position in the array.

Time complexity     -   O(nlog N) - Best.   Worst - O(n^2)
Space complexity    -   O(log n)
"""


def quick_sort(array, left, right):
    if left < right:
        # print(f"array = {array}     left = {left} right = {right}")
        partition_index = partition(array, left, right)
        quick_sort(array, left, partition_index - 1)
        quick_sort(array, partition_index + 1, right)


def partition(array, left, right):
    # sort array in way that all elements that less than pivot are to the left to the pivot
    # and all elements that more than pivot are to the right to the pivot
    # return the pivot index
    pivot_index = choose_pivot(array, left, right)
    pivot = array[pivot_index]
    left_index = left
    right_index = right
    while left_index <= right_index:
        # print(f"left_index = {left_index} right_index = {right_index}")
        # find element from left part of the array that more than pivot
        while array[left_index] <= pivot and left_index < right:
            left_index += 1
        # find element from right part of the array that less than pivot
        while array[right_index] >= pivot and right_index > left:
            right_index -= 1
        if left_index >= right_index:
            break
        # swap those elements
        array[left_index], array[right_index] = array[right_index], array[left_index]
    # swap pivot element with element that stands on pivot's place in array
    array[left_index], array[pivot_index] = array[pivot_index], array[left_index]
    return left_index


def choose_pivot(array, left, right):
    """
    Take the last element of array as pivot.
    :param array:
    :param left:
    :param right:
    :return:
    """
    return right


number = [3, 7, 8, 5, 2, 1, 9, 5, 4]
number2 = [0, 99, 44, 6, 2, 99, 1, 5, 63, 63, 87, 283, 4, 0, 0]
number3 = [6, 5, 3, 1, 8, 7, 2, 4]
print(number)
quick_sort(number, 0, len(number) - 1)

print(number2)
quick_sort(number2, 0, len(number2) - 1)
print(number2)

print(number3)
quick_sort(number3, 0, len(number3) - 1)
print(number3)
