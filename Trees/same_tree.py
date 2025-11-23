"""
LeetCode  - Same Tree
Difficulty: Easy
https://leetcode.com/problems/same-tree/description/

Problem:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Approach:

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:

        # Check the values and structures
        # if both are none

        if not p and not q:
            return True

        # if only one is none -> dif
        if not p or not q:
            return False

        #verify the val
        if p.val!=q.val:
            return False

        # Keep verifying

        
        # Pass all tests

        return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))