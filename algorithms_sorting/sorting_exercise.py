# 1 - Sort 10 schools around your house by distance:
# Insertion
# Fast for small input, easy to code. Space complexity - O(1)

# 2 - eBay sorts listings by the current Bid amount:
# Radix or Counting
# Limited count of bid amount (usually from 1$ to hundreds $). Time complexity - better than O(nlogn)

# 3 - Sport scores on ESPN
# Quick
# It can be a lot of different types of scores. Quick has compromise between time and space complexity.

# 4 - Massive database (can't fit all into memory) needs to sort through past year's user data
# Heap sort
# Space complexity - O(1)
# or
# Merge
# This dataset is already too much than a computer can handle
# so you would most likely process it in a distributed manner,
# or by chunking the data, in which case, space is not your main concern,
# but rather the time complexity.
#

# 5 - Almost sorted Udemy review data needs to update and add 2 new reviews
# Insertion
# Because of the presorted list

# 6 - Temperature Records for the past 50 years in Canada
# Radix or Counting
# If data doesn't have decimal places
# Quick
# If data have decimal places. And we can do some in memory sorting. Save on space complexity

# 7 - Large user name database needs to be sorted. Data is very random.
# Merge
# If we have enough memory and memory isn't too expensive
# Quick
# To save on space complexity. And if can pick a good pivot.

# 8 - You want to teach sorting for the first time
# Bubble sort
# Selection

