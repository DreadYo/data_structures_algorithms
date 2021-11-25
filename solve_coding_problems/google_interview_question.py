
"""
1. When the interviewer says the question,
write down the key points at the top (i.e. sorted array).
Make sure you have all the details. Show how organized you are.
"""

# This question is same as that in the Google interview question video.
# We are given an array of integers and a particular sum.
# We have to check if there are any two elements in the array that add up to the given sum.
# For example,
# array = [1,2,3,9] ,sum = 8
# This should return False
# array = [1,2,4,4] ,sum = 8
# This should return True as 4+4=8

# Array and sum are given by user's input
# Array - sorted

"""
2. Make sure you double check: What are the inputs? What are the outputs?
"""

# inputs: 2 parameters (array and sum)
# You can ask interviewer if they are always going to be arrays
# Is it possible that the input might not be array, maybe an object, maybe a string?
# output: True/False

"""
3. What is the most important value of the problem?
Do you have time, and space and memory, etc.. 
What is the main goal?
"""

# May ask how large this arrays is going to get?
# If arrays are always not large, than you don't have to worry about big-O, time and space complexity.
# Ask what's more important: time  complexity, space complexity?

# Assume that arrays - no size limit

"""
4. Don't be annoying and ask too many questions.
"""

# Asl only needed questions

"""
5. Start with the naive/brute force approach.
First thing that comes into mind.
It shows that you’re able to think well and critically
(you don't need to write this code, just speak about it).
"""

# Now, the very first solution that comes to mind is the naive, or brute force solution.
# So let's code that down.
# Complexity. O(n^2).

array1 = [1,2,3,9]
array2 = [1,2,4,4]
sum = 8


def brute_force_solution(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                return True
    return False

print(brute_force_solution(array1, sum))


"""
6. Tell them why this approach is not the best
(i.e. O(n^2) or higher, not readable, etc...)
"""

# It's too slow. And when input size gets large, solution becomes very inefficient.


"""
7. Walk through your approach, comment things and see where you may be able to break things. 
Any repetition, bottlenecks like O(N^2), or unnecessary work? 
Did you use all the information the interviewer gave you? 
Bottleneck is the part of the code with the biggest Big O. 
Focus on that. Sometimes this occurs with repeated work as well.
"""

# O(n^2) is too slow. I try to find something more efficient.
# One solution better than O(n^2) that comes to mind is :
# We loop through the array once and for every element we encounter,
# we calculate its complement,i.e., the number which when added
# to the element at hand, will give the sum.
# Then we do a binary search for this complement in the remaining portion of the array
# Since binary search is O(log n) and we loop through the array once,
# the overall complexity is O(nlog n), which is better than O(n^2)

# We have arrived at an O(nlog n) function from the naive O(n^2)
# But this is still not great and it seems like there is some scope for improvement.
# Lets try to make it O(n)

# We take one element from the beginning of the array (left) and one from the end of the array (right).
# Than we calculate their sum. If it equals the given sum, return True (job done!)
# If given sum is greater than what we get, it means that we needed greater sum, and
# than we take the next element from the left (instead of the first).
# If given sum is less than what we get, it means that we needed less sum, and
# than we take the previous element from the right (instead of the last).
# and we keep moving until we find needed pair of elements or until the left and right indices cross
# Since this procedure requires only one moving through array, the complexity is O(n)!

def pair_sum(arr, sum):
    left = 0
    right = len(arr) - 1
    while left < right:
        my_sum = arr[left] + arr[right]
        if my_sum == sum:
            return True
        elif my_sum < sum:
            left += 1
        elif my_sum > sum:
            right -= 1
    return False

print(pair_sum(array1, sum))
print(pair_sum(array2, sum))

# Time complexity is O(n) because we have the assumption that the array is sorted
# What if the array isn't sorted?
# In that case the first solution that comes to mind is that we can sort the array in O(nlog n) time
# And then perform the pair_sum operation on the sorted array to give us a final time complexity of O(nlog n)
# Python's built-in sort method uses Tim Sort which has an average case time coplexity of O(nlog n)
# So we can simply use that, or use a different sorting algorithm such as quicksort or heapsort.
# Here, we are going with the built-in method

def sort_pair_sum(arr, sum):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        my_sum = arr[left] + arr[right]
        if my_sum == sum:
            return True
        elif my_sum < sum:
            left += 1
        elif my_sum > sum:
            right -= 1
    return False


# This solves our problem if the array is unsorted to begin with.
# But we have lost out on time complexity as we have gone from O(n) to O(nlog n)
# One thing we can do to get back to O(n) complexity is :

# We can use some collection with fast (O(1)) access operation (hash tables).
# We can create a dictionary (in python) when we go through array and put the element of this array
# into the dictionary if the complement (sum - element) of
# the sum and element from array isn't already present in dictionary.
# And if this value IS present in the dictionary, than we return True, because it's our needed element.

# It will take us O(n) to go through array put values into the dictionary and check the sum

"""
8. Before you start coding, walk through your code and write down the steps you are going to follow.
"""

# def unsorted_pair_sum(arr, sum):
    # create dictionary
    # loop through array:
        # and check if (sum-element) exists in dictionary
        # if exists "Jobe done!"
        # if not - put array's element into the dictionary


"""
9. Modularize your code from the very beginning. 
Break up your code into beautiful small pieces and add just comments if you need to.
"""

# If function is doing too many things, it is a good idea to separate it into few smaller functions.
# Do it. Or say about it on the interview.

"""
10. Start actually writing your code now. 
Keep in mind that the more you prepare and understand what you need to code, 
the better the whiteboard will go. 
So never start a whiteboard interview not being sure of how things are going to work out. 
That is a recipe for disaster. 
Keep in mind: A lot of interviews ask questions that you won’t be able to fully answer on time. 
So think: What can I show in order to show that I can do this and I am better than other coders. 
Break things up in Functions 
(if you can’t remember a method, just make up a function and you will at least have it there. 
Write something, and start with the easy part.
"""

def unsorted_pair_sum(arr, sum):
    # create dictionary
    complements = dict()
    # loop through array:
    for element in arr:
        compl = sum - element
        # and check if (sum-element) exists in dictionary
        if compl in complements:
            # if exists "Jobe done!"
            return True
        else:
            # if not - put array's element into the dictionary
            complements[element] = True
    return False


print(unsorted_pair_sum(array1, sum))
print(unsorted_pair_sum(array2, sum))


"""
11. Think about error checks and how you can break this code. 
Never make assumptions about the input. 
Assume people are trying to break your code and that Darth Vader is using your function. 
How will you safeguard it? Always check for false inputs that you don’t want. 
Here is a trick: Comment in the code, the checks that you want to do... 
write the function, then tell the interviewer that you would write tests now to make 
your function fail (but you won't need to actually write the tests).
"""

# In previous solution I didn't check if input are arrays.
# What happens if I don't have second parameter or I have None instead of array?
# Add error message if input is incorrect.

def try_unsorted_pair_sum(arr, sum):
    try:
        # create dictionary
        complements = dict()
        # loop through array:
        for element in arr:
            compl = sum - element
            # and check if (sum-element) exists in dictionary
            if compl in complements:
                # if exists "Jobe done!"
                return True
            else:
                # if not - put array's element into the dictionary
                complements[element] = True
        return False
    except TypeError:
        return "Exactly array and number required"


print(try_unsorted_pair_sum([None], 2))
print(try_unsorted_pair_sum(["ed", "as"], "d"))


"""
12. Don’t use bad/confusing names like i and j. Write code that reads well.
"""

"""
13. Test your code: Check for no params, 0, undefined, null, massive arrays, async code, etc... 
Ask the interviewer if we can make assumption about the code. 
Can you make the answer return an error? Poke holes into your solution. 
Are you repeating yourself?
"""

# I can say that I can write Unit tests to test this code.

# import unittest
# from solve_coding_problems.google_interview_question import try_unsorted_pair_sum
#
#
# class PairSumTests(unittest.TestCase):
#     """check False result"""
#     def test_false_result(self):
#         self.assertFalse(try_unsorted_pair_sum([1, 2, 3, 9], 8),
#                          "we should get False, because we don't have needed pair")
#
#     def test_true_result(self):
#         """check True result"""
#         self.assertTrue(try_unsorted_pair_sum([1, 2, 4, 4], 8),
#                         "we should get True, because we have needed pair")
#
#     def test_wrong_types(self):
#         """check wrong inputs"""
#         self.assertEqual(try_unsorted_pair_sum([None], 2), "Exactly array and number required")
#
#
# if __name__ == "__main__":
#     unittest.main()

"""
14. Finally talk to the interviewer where you would improve the code. 
Does it work? Are there different approaches? Is it readable? 
What would you google to improve? How can performance be improved? 
Possibly: Ask the interviewer what was the most interesting solution you have seen to this problem
"""

# Maybe the more readable solution exists

"""
15. If your interviewer is happy with the solution, the interview usually ends here. 
It is also common that the interviewer asks you extension questions, 
such as how you would handle the problem if the whole input is too large to fit into memory, 
or if the input arrives as a stream. 
This is a common follow-up question at Google, where they care a lot about scale. 
The answer is usually a divide-and-conquer approach — perform distributed processing of the data 
and only read certain chunks of the input from disk into memory, 
write the output back to disk and combine them later.
"""


# If array ise very large to fit into memory.
# Then we can also speak about Space complexity

# The the first solution (with nested loops)
# have Space complexity - O(1).
# Because there are not created any variables and space complexity for function is constant.

# def brute_force_solution(arr, sum):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == sum:
#                 return True
#     return False


# In solution with dictionary was created new object (dictionary).
# Space complexity - O(n) when n - is a length of array

