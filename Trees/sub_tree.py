"""
LeetCode  - Subtree of Another Tree
Difficulty: Easy
https://leetcode.com/problems/subtree-of-another-tree/description/

Problem:

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


Approach:

"""


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isSubtree(self, root, subRoot):
        print("isSubtree called on:", root.val if root else None)

        #base cases
        if not subRoot:
            return True

        if not root:
            return False

        # Checa se a subárvore começa neste nó
        print("  checking at node (root):", root.val)
        if self.check_trees(root, subRoot):
            print("  match found at node", root.val)
            return True
        
        # this did not work, so i should continue

        #print('Going left from ', root.left.val)
        left_node = self.isSubtree(root.left,subRoot)
        #print("  left_result for", root.left.val, "=", left_node)

        if left_node:
            return True

        #print('Going right from', root.right.val)
        right_node = self.isSubtree(root.right,subRoot)
        #print(" right_result for", root.right.val, '=', right_node)

        if right_node:
            return True
        
        return False
        


    def check_trees(self,tree1,tree2):
        # I should always test for the sub tree1
        # There are 3 ways 2 trees can be the same 


        # They are empty
        if not tree1 and not tree2:
            return True

        # Only one is empty 
        if not tree1 or not tree2:
            return False

        # now check value
        if tree1.val != tree2.val:
            return False

        return self.check_trees(tree1.left,tree2.left) and self.check_trees(tree1.right,tree2.right)

        



    
        
