"""
Selection sort
involves finding the minimum element in one pass through the array
and then swapping it with the first position of the unsorted part of the array.

Time complexity     -   O(n^2) in all cases
Space complexity    -   O(1)
"""


def selection_sort(array):
    # -1 because when only 1 element remains, it will be already be sorted
    for i in range(len(array)-1):
        # Set the index of minimum element to be the ith index
        smallest_index = i
        # Check the array from the i+1th element to the end
        for j in range(i+1, len(array)):
            # If a smaller element than the minimum element is found,
            # re-assign the index of the minimum element
            if array[j] < array[smallest_index]:
                smallest_index = j
        # If smallest_index has changed, i.e, a smaller  element has been found,
        # then swap that element with the ith element
        if smallest_index != i:
            array[i], array[smallest_index] = array[smallest_index], array[i]


number = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(number)
print()
selection_sort(number)
print()
print(number)
