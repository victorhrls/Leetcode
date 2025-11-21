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
        # First i need to find the half way 
        
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        # Slow will pont to the half of the list
        
        second = slow.next # slice the list in two halfs
        slow.next = None   # The list ended
        
        
        first = head    # first half
        second = self.reverse_list(second)  # second half inverted
        
        
        while first and second:
            
            temp_first = first.next
            temp_second = second.next
            
            first.next = second
            second.next = temp_first
            
            first = temp_first
            second = temp_second
        
        
        
        
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
        
        