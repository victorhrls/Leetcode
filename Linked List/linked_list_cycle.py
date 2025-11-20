"""
LeetCode  - Linked List Cycle
Difficulty: Easy
https://leetcode.com/problems/linked-list-cycle/description/

Problem:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Approach:

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        
        # To make sure any node was already visited, i will use a set
        
        # I have to store the address and value
        visited = set()
        
        while head:
            if head in visited: # It is in the set
                return True
            visited.add(head)
            head = head.next
            
        
    
        return False
        
        
        

# Is there a cycle on the list ?
# Use POS to find out

def test(val):
    dummy = ListNode()
    curr = dummy
    for v in val:
        curr.next = val
        curr = curr.next
    
    return dummy.next