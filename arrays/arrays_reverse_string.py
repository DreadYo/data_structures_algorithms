# Create a function that reverses a string
# 'Hi My name is Albert' should be 'treblA si eman yM iH'

# The first solution that comes to mind is
# we can create a new array and append the characters of the original array,
# one by one from the end to the beginning.

def reverse(string):
    # check input
    if not string or type(string) != str or len(string) < 2:
        return "Wrong input"
    new_lst = []
    # The for loop runs from the last element to the first element of the original string
    for i in range(len(string) - 1, -1, -1):    # Time complexity - O(n)
        # The characters of the original string are added to the new string
        new_lst.append(string[i])
    # The characters of the reversed array are joined to form a string
    return "".join(new_lst)                     # Time complexity of join - O(n)

# All time complexity - O(n)
# But since we are also creating a new array of the same size ,
# the space complexity is also O(n)

# Because strings in Python are immutable you have to use another structure to store result.
# Even if you create solution when you will swap elements from beginning and end of the string,
# in this operation you should create new string or list every time.
# And space complexity wan't be less than O(n)

# The simplest and more readable way to use built-in functions and Python slices


def reverse_simple(string):
    return string[::-1]


def reverse_simple2(string):
    return reverse(string)


print(reverse("Hi My name is Albert"))


print(reverse_simple("Hi My name is Albert"))
print(reverse_simple2("Hi My name is Albert"))
