"""
283. Move Zeroes (Leetcode)

Given an integer array nums,
move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]


Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?
"""

# The first solution that I comes to mind, as always, it's the brute force solution

def move_zeroes_brute_force(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)     # O(n) * n
            nums.append(0)  # O(1) * n


nums1 = [0, 1, 0, 3, 12]
move_zeroes_brute_force(nums1)
print(nums1)

# Time complexity of this solution - O(n^2)
# It's too slow.

# I'll try to create more efficient solution.

def move_zeroes(nums):
    arr = []
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
        else:
            arr.append(nums[i])     # O(1) * n
    for _ in range(zero_count):
        arr.append(0)
    nums[:] = arr[:]


nums2 = [0, 1, 0, 3, 12]
move_zeroes(nums2)
print(nums2)

# Time complexity of this solution - O(n)
# But this solution used additional array

# I try to use only exists array
def move_zeroes2(nums):
    zero_count = 0
    count = len(nums)
    for i in range(count):
        if nums[i] == 0:
            zero_count += 1
        else:
            nums.append(nums[i])    # O(n)
    for _ in range(zero_count):
        nums.append(0)              # O(n)
    del nums[:count]                # O(n^2)

nums3 = [0, 1, 0, 3, 12]
move_zeroes2(nums3)
print(nums3)

# Time Complexity - O(n^2)
# Unefficient solution, because delete from array is a very heavy operation


# I'll try to go through array and swap every non-zero element I find with the first un-swapped zero.

def move_zeroes3(nums):
    z = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[z] = nums[z], nums[i]
            z += 1

nums4 = [0, 1, 0, 3, 12]
move_zeroes3(nums4)
print(nums4)

# In this solution I traverse the array and
# swap every non-zero element with itself until I find a 0.
# Then I swap the next non-zero element with the 0 and
# I keep doing this until I have looped over the entire array.
# This seems like a cleaner solution to the first one
# but still there are lots of unnecessary swaps going on here.
# Still, I looping over the array once and the swapping is done in constant time,
# so overall time complexity is O(n)

# A very elegant solution to this problem can be the following one-liner :

def one_liner_move(array):
    array.sort(key=bool, reverse=True)
    return array

nums5 = [0, 1, 0, 3, 12]
print(one_liner_move(nums5))

# What this does is it sorts the array in place using the key as boolean.
# Now the integer 0 is considered as boolean 0 and all other integers are considered as boolean 1
# So providing the key as bool, we are telling the sort method to sort the array on the basis of boolean values
# The 0's , which are considered as 0, come first,
# and the remaining numbers, considered as 1, come next, in their original order.
# The reverse=True reverses this arrangement so that the 0's are all the end and the non-zero numbers at the front.
# The complexity for this is O(nlog n) as the complexity of Python's built-in sort method is O(nlog n)
