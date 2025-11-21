"""
LeetCode  - Reorder List
Difficulty: Medium
https://leetcode.com/problems/reorder-list/

Problem:

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Approach:

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        # So i will just MODIFY HEAP
        
        # The nodes n1 -> n2 -> n3 ... nn will be
        # n1 -> nn -> n2 -> nn-1 -> n3 .... 
        
        # So we can check two patterns 
        
        # First n1-> n2 -> n3 ... between the other nodes
        
        # I can have two pointers .
        
        # one pointer will check for n1-> n2 -> n3 ...
        
        # The other pointer will be Nn -> nn-1 -> nn-2 ... (Backwards)
                
        reverse = reverse_list(head)
        
        
    def reverse_list(head):
        
        reverse = None
        
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = reverse
            
            reverse = curr
            curr = temp
            
        return reverse
        
        
    
    
test =[1,2,3,4] 
result = [1,4,2,3]
        
        