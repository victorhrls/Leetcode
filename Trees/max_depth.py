"""
LeetCode  - Invert Binary tree
Difficulty: Easy
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Problem:
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.


Approach:

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        # Depth First Search 
        if not root:
            return 0
        

        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
                
                
        # Each time i run it will go more depth 
        # and increase 1 
        # and i keep this value on left_depth
                
        return 1 + max(left_depth,right_depth)
        