# The elements of an array are stored in contiguous memory locations
# Arrays are of two types : Static and Dynamic
# Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
# In Python we only have dynamic arrays

# lookup/access -   O(1)
# push/pop      -   O(1)
# insert        -   O(n)
# delete        -   O(n)


array = ['a', 'b', 'c', 'd']

# lookup/access
array[2]              # O(1)

# push
array.append('e')     # O(1)

# pop
array.pop()           # O(1)

# insert
array.insert(2, 'y')  # O(n)
array.insert(0, 'x')  # O(n)

# delete              # O(n)
# by index
array.pop(2)
print(array)

# by value
array.remove('c')
print(array)

# by position from 2nd to 4th
del array[1:3]
print(array)

