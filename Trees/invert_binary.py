"""
LeetCode  - Invert Binary tree
Difficulty: Easy
https://neetcode.io/problems/invert-a-binary-tree/question?list=blind75


Problem:
You are given the root of a binary tree root. Invert the binary tree and return its root.

Approach:

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        # Depth First Search -> Prioritize DEPTH

        if not root:
            return None
        
        curr = root
        if curr:
            # Temporary to keep the left and right
            temp_right = curr.right # original sub tree left
            temp_left = curr.left  # origianl sub tree right

            # CHANGE NODES
            curr.right = temp_left # new tree right
            curr.left = temp_right # new tree left

            # Run through the nodes
            if curr.left:
                self.invertTree(curr.left)
            if curr.right:
                self.invertTree(curr.right)

        return root


        