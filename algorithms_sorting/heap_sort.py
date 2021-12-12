"""
Heap Sort as the name suggests, uses the heap data structure.
First the array is converted into a binary heap.
Then the first element which is the maximum element in case of a max-heap,
is swapped with the last element
so that the maximum element goes to the end of the array
as it should be in a sorted array.
Then the heap size is reduced by 1 and max-heapify function is called on the root.

Time complexity     -   O(nlog N) in all cases
Space complexity    -   O(1)
"""


def max_heapify(array, heap_size, i):
    # check all children of current node (index i) to agree Max Binary Heap rule:
    # all children have to be less than parent
    # If not,
    # replace parent with max of children and check (and replace if need) recursively their children
    # Time complexity     -   O(log n)
    print("max_heapify start")
    print(f"array = {array}     heap_size = {heap_size}     i = {i}")
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    print(f"left = {left}     right = {right}     largest = {largest}")
    if left < heap_size:
        print(f"array[left] = {array[left]}     array[largest] = {array[largest]}")
        if array[left] > array[largest]:
            largest = left
    if right < heap_size:
        print(f"array[right] = {array[right]}     array[largest] = {array[largest]}")
        if array[right] > array[largest]:
            largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heap_size, largest)
    print("max_heapify end")


def build_heap(array):
    # build Max Binary Heap using unsorted array
    # Time complexity     -   O(nlog n)
    heap_size = len(array)
    # begin from the middle of the array and go backward
    # Because nodes in the second part of array don't have children
    for i in range((heap_size//2), -1, -1):     # O(n)
        max_heapify(array, heap_size, i)        # O(log n)


def heap_sort(array):
    # Time complexity     -   O(nlog n)
    heap_size = len(array)
    # build correct Max Binary Heap using array
    build_heap(array)           # O(nlog n)
    print(f'Heap : {array}')
    # go backward through array from the end to the beginning
    for i in range(heap_size-1, 0, -1):     # O(n)
        # replace first and last items
        # Last item begin the largest, because girst was the largest in the Max Binary Heap
        array[0], array[i] = array[i], array[0]
        # reduce length of the heap
        heap_size -= 1
        # modify remaining heap to accord Max Binary Heap rules
        max_heapify(array, heap_size, 0)        # O(log n)


if __name__ == "__main__":
    number = [2, 8, 1, 4, 14, 7, 16, 10, 9, 3]
    print(number)
    heap_sort(number)
    print(number)
