"""
Validate Binary Search Tree (Leetcode 98)

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
 - The left subtree of a node contains only nodes with keys less than the node's key.
 - The right subtree of a node contains only nodes with keys greater than the node's key.
 - Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

Solution:
The way it works is, it recursively adds the max and mins.
so as it gets deeper the min/max will be root depending on what side the tree goes
solved initially by just checking if the parent node was greater than left and less than right
but this didn't account for a condition where the right side of the tree,
contained a node that had a value less than the root.

"""

import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    return traverse_tree(root, -math.inf, math.inf)


def traverse_tree(root, minimum, maximum):
    if not root:
        return True
    if root.val <= minimum or root.val >= maximum:
        return False
    return traverse_tree(root.left, minimum, root.val) and traverse_tree(root.right, root.val, maximum)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    root1 = TreeNode(2, node1, node2)
    print(is_valid_bst(root1))

    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node4 = TreeNode(4, node3, node6)
    root2 = TreeNode(5, node1, node4)

    print(is_valid_bst(root2))

    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node7 = TreeNode(7)
    node6 = TreeNode(6, node3, node7)
    root2 = TreeNode(5, node4, node6)

    print(is_valid_bst(root2))

