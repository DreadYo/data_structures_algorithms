# Google Question
# Given an array, return the first recurring character
# Example1 : array = [2,1,4,2,6,5,1,4]
# It should return 2
# Example 2 : array = [2,6,4,6,1,3,8,1,2]
# It should return 6

# The first solution that comes to mind, as always, it's brute force solution
# Using 2 nested loops.
# In outer loop we go through array (using index i)
# In nested loop runs from 0 to i
# (on i-iteration we check if i-element equal to any element behind it)


def first_reccur_brute(array):
    # check input
    if not array or len(array) < 2:
        return "undefined"
    for i in range(len(array)):
        for j in range(i):
            if array[i] == array[j]:
                return array[i]
    return "undefined"


print(first_reccur_brute([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(first_reccur_brute([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_reccur_brute([2, 3, 4, 5]))
print(first_reccur_brute([]))
print(first_reccur_brute([2]))

# Time complexity - O(n^2)
# Space complexity - O(1)

# It's too slow.
# I can find more efficient solution.

# we can create a dictionary and keep storing each element
# of the array in the dictionary as we go along the array.
# But before adding the element to the dictionary,
# we'll check if the element is already present in the dictionary
# If yes, then we simply return the element and break out
# If not, then we add the element to the dictionary and move forward


def first_reccur(array):
    # check input
    if not array or len(array) < 2:
        return "undefined"
    dict_array = {}
    for el in array:
        if el in dict_array:
            return el
        else:
            dict_array[el] = True
    return "undefined"


print(first_reccur([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(first_reccur([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_reccur([2, 3, 4, 5]))
print(first_reccur([]))
print(first_reccur([2]))

# Time complexity - O(n)
# Space complexity - O(n)

# The time complexity is O(n) as we are looping through the array only once
# And the search which we are doing in the dictionary,
# is of O(1) time, since it is basically an implementation of hash table.

