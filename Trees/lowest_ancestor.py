"""
LeetCode  - Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


Problem:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Approach:

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # First let's see what is the biggest here
        
        #if p.val>q.val:
        #    big = p
        #    small = q
        #else:
        #    big = q
        #    small = p
        
        # case 1 - root is none
        if root is None:
            return None

        # Binary search tree : left is smaller and right is bigger 

        # case 2 - descendent of itself 
        # Descendent left and right
        #if big.left == small:
        #    return big
        #
        #if small.right == big:
        #    return small

        # case 3 - two nodes form the same node 

        if p.val< root.val and q.val < root.val: #both are lower
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val : # both are on the right
            return self.lowestCommonAncestor(root.right,p,q)
        
        else:
            # If one is smaller and other bigger
            # If one of them is equal to the root
            return root


      

        