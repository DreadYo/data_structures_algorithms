"""
Merge Sort
uses the Divide and Conquer approach.
It involves breaking up the array from the middle until
Arrays of only 1 elements remain and then merging them back up in a sorted order.

Time complexity     -   O(nlog N)
Space complexity    -   O(n)
"""

def merge_sort(array):
    length = len(array)
    # base case to stop recursion
    if length == 1:
        return array
    # split array in into right and left
    middle = length // 2
    left = array[:middle]
    right = array[middle:]
    print(f"left = {left} right = {right}")

    return merge(merge_sort(left),
                 merge_sort(right))


def merge(left, right):
    arr = []
    print(left, right)
    left_index = 0
    right_index = 0
    # go through 2 sorted arrays: left and right
    # and compare elements and put elements from those 2 arrays in new array arr in sorted way
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            arr.append(left[left_index])
            left_index += 1
        else:
            arr.append(right[right_index])
            right_index += 1
    # add in array arr existing elements from left array
    arr.extend(left[left_index:])
    # add in array arr existing elements from right array
    arr.extend(right[right_index:])
    print(f"arr = {arr}")
    return arr


number = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# number = [6, 5, 3, 1, 8, 7, 2, 4]
print(number)
print(merge_sort(number))
