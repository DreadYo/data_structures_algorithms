"""
Insertion sort
For the first iteration we fix the first element, assuming it is at its correct position
Then we loop through the rest of the elements and insert them in their correct positions,
with respect to the already sorted part of the array
Time complexity is O(n^2) in worst case. In best - O(n), when the list is almost sort or small datasets.
"""


def insertion_sort(array):
    count = 0
    # go through array
    for i in range(len(array)):
        # store index for current element in current_index
        current_index = i
        # go backward through elements of array left to current element
        for j in range(i-1, -1, -1):
            count += 1
            # and compare with current element
            # if current element less than element to the left of it
            if array[current_index] < array[j]:
                # then swap those elements and continue compare
                # (because all elements to the left of the current element are sorted,
                # then at the end of comparision current element finds his place in array)
                array[current_index], array[j] = array[j], array[current_index]
                current_index -= 1
            # else don't need to go to the beginning of the array if element finds his place
            else:
                break
    print(count)


number = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(number)
insertion_sort(number)
print(number)

number2 = [9, 8, 7, 6, 5]
print(number2)
insertion_sort(number2)
print(number2)

number3 = [5, 6, 7, 9, 8]
print(number3)
insertion_sort(number3)
print(number3)
