"""
189. Rotate Array (Leetcode)
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


# The first solution that comes to mind, as always, it's brute force solution
# Rotate the array by 1 element in each traversal of the array.

def rotate_brute_force(nums, k) -> None:
    for _ in range(k):
        last = nums[-1]
        for i in range(len(nums)):
            nums[len(nums) - 1 - i] = nums[len(nums) - 2 - i]
        nums[0] = last


nums1 = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_brute_force(nums1, k)
print(nums1)


# Time complexity - O(n*k)
# Space complexity - O(1)


# Create a new array.
# Go through array and assign to current position the element from old array,
# which had position less on k.

def rotate_array(nums, k) -> None:
    length = len(nums)
    new_arr = [None for _ in range(length)]
    for i in range(length):
        new_arr[length - 1 - i] = nums[length - 1 - i - k%length]
    nums[:] = new_arr[:]


nums2 = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums2, k)
print(nums2)


# Time complexity - O(n)
# Space complexity - O(n)


# The more efficient solution will be using reversal algorithm.
# At first, reverse all array,
# than reverse back first k elements,
# and reverse back last n-k elements.

def rotate_reverse(nums, k) -> None:
    array = reverse(nums, 0, len(nums) - 1)
    array = reverse(nums, 0, k % len(array) - 1)
    array = reverse(nums, k % len(array), len(nums) - 1)


def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


nums3 = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_reverse(nums3, k)
print(nums3)

# Time complexity - O(n)
# Space complexity - O(1)