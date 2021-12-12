"""
Comparison sort:
Insertion sort      -   small input or input almost sorted
Bubble sort         -   only for education purposes
Selection sort      -   only for education purposes
Merge sort          -   Really good - O(nlogn), but expensive O(n)
Quick sort          -   Better than Merge, but have bad worst case - O(n^2) - you should pick pivot properly.
Heap sort           -


Heap sort has a worst- and average-case running time of O(nlogn) like Merge sort,
but Heap sort uses O(1) auxiliary space (since it is an in-place sort)
while Merge sort takes up O(n) auxiliary space,
so if memory concerns are an issue, Heap sort might be a good, fast choice for a sorting algorithm.

Quick sort has an average-case running time of O(nlogn) but has notoriously better constant factors,
making Quick sort faster than other O(nlogn)-time sorting algorithms.
However, Quick sort has a worst-case running time of O(n^2) and a worst-case space complexity of O(logn),
so if it is very important to have a fast worst-case running time and efficient space usage,
Heap sort is the best option.
Note, though, that Heap sort is slower than Quick sort on average in most cases.

Timsort Algorithm
The Python way is a hybrid sorting algorithm which is derived from
merge and insertion sort.
For smaller runs (up to a minimum run size of 64) Timsort internally picks insertion sort,
otherwise merge sort is being used.
Its worst-case and average complexity is O(n log n), but the best-case performance is O(n).

Use cases of the sort algorithm
The sorting algorithm is implemented as list.sort() or sorted(list).
The difference between these two implementations is that list.sort() rearranges
the original list while sorted(list) returns a new list.



Non-Comparison sort:
Counting sort

Radix sort

"""
