"""
https://coderbyte.com/editor/Longest%20Word:JavaScript
Have the function LongestWord(sen) take the sen parameter
being passed and return the longest word in the string.
If there are two or more words that are the same length,
return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty.
Words may also contain numbers, for example "Hello world123 567"

Examples
Input: "fun&!! time"
Output: time

Input: "I love dogs"
Output: love
"""

# The first solution that comes to mind, as always, it's brute force solution
# I check for every character if it's an alphanumeric or not.
# If it is, I increase a counter and update a variable which stores the maximum value of counter.
# If I see a non-alphanumeric character, I reset the counter to zero and start again
# when the next alphanumeric arrives

def longest_word_brute(sen):
    count = 0
    maximum = 0
    words = []
    word = []
    for char in sen:
        if char.isalnum():
            count += 1
            word.append(char)
        else:
            if word not in words and word:
                words.append(''.join(word))
                word = []
            maximum = max(maximum, count)
            count = 0
    maximum = max(maximum, count)
    if word not in words and word:
        words.append(''.join(word))
    for item in words:
        if len(item) == maximum:
            return item


print(longest_word_brute("fun&!! time"))
print(longest_word_brute("I love dogs"))

# Too complicated solution - unefficient
# Time complexity - O(m*n)
# Space complexity - O(m+n)

# I'll try to solve this problem without creating new arrays
# I go through string like in previous solution
# but I don't create arrays and put words in it
# Instead of it, I keep index of the beginning of new word (minus 1)
# and keep index of the largest word (minus 1)
# At he end of function I will have length of the largest word in var maximum
# and index of this word in string
# Then I return a slice from string

def longest_word(sen):
    count = 0
    maximum = 0
    index = -1
    max_index = 0
    for i in range(len(sen)):
        if sen[i].isalnum():
            count += 1
        else:
            if count > maximum:
                maximum = count
                max_index = index
            count = 0
            index = i
    if count > maximum:
        maximum = count
        max_index = index
    max_index += 1
    return sen[max_index:max_index+maximum]


# Time complexity - O(n)
# Space complexity - O(1)

print(longest_word("fun&!! time"))
print(longest_word("I love dogs"))

# Regex solution

import re

def regex(string):
    string = re.findall('\w+', string)
    maximum = max([len(item) for item in string])
    for item in string:
        if len(item) == maximum:
            return item
sss = "Hello there how are you"
print(regex(sss))

