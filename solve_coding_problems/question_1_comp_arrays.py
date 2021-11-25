
"""
1. When the interviewer says the question,
write down the key points at the top (i.e. sorted array).
Make sure you have all the details. Show how organized you are.
"""

# Given two arrays.
# Create a function that let's a user know (true/false) whether
# these two arrays contain any common items
# For example:
# array1 = ['a','b','c','x']
# array2 = ['z','y','i']
# should return True as element 'x' appears in both arrays.
# -------------------------------
# array1 = ['a','b','c','x']
# array2 = ['z','y','x']
# should return False.

"""
2. Make sure you double check: What are the inputs? What are the outputs?
"""
# inputs: 2 parameters (arrays)
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
# Complexity. At first, it looks like O(n^2). But arrays can have different lengths.
# Then O(m*n)

array1 = ['a','b','c','x']
array2 = ['x','y','z']


def brute_force_sol(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return True
    return False


print(brute_force_sol(array1, array2))


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

# O(n*m) is too slow.I try to find something more efficient.
# I try to use some collection with fast (O(1)) access operation (hash tables).
# I will store in this collection one of arrays.
# It can be dictionary. It will take me O(n) to put all elements from array to dictionary.
# Then I go through another array and check if element from this array is presented in dictionary.
# It takes - O(m)
# All complexity - O(m+n)

"""
8. Before you start coding, walk through your code and write down the steps you are going to follow.
"""

# def dict_sol(arr1, arr2):
    # loop through first array and create dictionary where
    # keys = items in the array

    # loop through second array and check
    # if item in second array exists on created dictionary.

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

# I don't need to check if the dictionary contains repetitive elements.
# Because dictionary in Python has unique keys.


def dict_sol(arr1, arr2):
    # loop through first array and create dictionary where
    # keys = items in the array
    dictionary = {el: True for el in arr1}
    # loop through second array and check
    # if item in second array exists on created dictionary.
    for el in arr2:
        if el in dictionary:
            return True
    return False


print(dict_sol(array1, array2))

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


def dict_sol2(arr1, arr2):
    try:
        dictionary = {el: True for el in arr1}
        for el in arr2:
            if el in dictionary:
                return True
        return False
    except TypeError:
        return "Exactly two arrays required"


print(dict_sol2(array1, array2))

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

# If arrays are very large to fit into memory.
# Then we can also speak about Space complexity

# The the first solution (with nested loops)
# have Space complexity - O(1).
# Because there are not created any variables and space complexity for function is constant.

# def brute_force_sol(arr1, arr2):
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             if arr1[i] == arr2[j]:
#                 return True
#     return False

# In solution with dictionary was created new object (dictionary).
# Space complexity - O(n) when n - is a length of array1

# def dict_sol2(arr1, arr2):
#     try:
#         dictionary = {el: True for el in arr1}
#         for el in arr2:
#             if el in dictionary:
#                 return True
#         return False
#     except TypeError:
#         return "Exactly two arrays required"
