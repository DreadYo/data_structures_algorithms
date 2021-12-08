"""
In Bubble Sort,
the largest value is bubbled up in every pass.
Every two adjacent items are compared and
they are swapped if they are in the wrong order.
This way, after every pass,
the largest element reaches to the end of the array.

Time complexity     -   O(n^2) (in Worst and Average Case),    O(n) - in best case
Space complexity    -   O(1)
"""


def bubble_sort(array):
    # -1 because when only 1 item will be left, we don't need to sort that
    for i in range(len(array)-1):
        # In every iteration of the outer loop, one number gets sorted.
        # So the inner loop will run only for the unsorted part
        for j in range(len(array)-1-i):
            # If two adjacent elements in the wrong order are found, they are swapped
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


number = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(number)
print()
bubble_sort(number)
print()
print(number)
