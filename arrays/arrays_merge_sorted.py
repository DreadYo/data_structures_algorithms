# Given 2 sorted arrays.
# Create function that gets those 2 arrays as parameters and
# merge them and return sorted array.

# Because arrays are sorted I will go through 2 arrays (from the beginning to end)
# I'll compare the corresponding elements of both arrays
# And add the smaller element to a new array and increment
# the index of the array from which the element was added.
# Again I will compare the elements of both arrays and repeat the procedure until all the elements have been added.


def merge_sorted_arrays(arr1, arr2):
    # check input
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    if arr1 is None or arr2 is None:
        return "Wrong input"
    new_arr = []
    i, j = 0, 0
    # The loop runs until I reach the end of one of the arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    # If one of the array's end wasn't reached I should add the remaining elements to the new array
    new_arr.extend(arr1[i:])
    new_arr.extend(arr2[j:])
    return new_arr

# Time complexity of this solution is O(n+m)
# Space complexity - O(n+m)

print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30, 42, 56, 78]))
