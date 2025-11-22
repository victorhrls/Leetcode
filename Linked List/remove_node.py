"""
LeetCode  - Remove Node
Difficulty: Medium
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Problem:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Approach:
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):

        # So i remove from the end ! 
        # So i will first reverse and then just count 

        reverse = self.reverse_node(head)

        
        if n==1: # i will already reverse
            # skip the head of the reversed
            new_rev = reverse.next if reverse else None
            # If reverse else none just to deal with empty 

            return self.reverse_node(new_rev)

        prev = reverse # POINTS TO THE HEAD, ALWAYS , 
        # PREV WILL BE THE POINTER I WILL MOVE ON THE HEAD
        count = 1
        while prev and count < n-1: # it will stop on the previous
            prev = prev.next
            count +=1        
        # now my pointer prev is on the n-1 node and i should just connect it 

        # should verify the existance

        if prev and prev.next:
            prev.next = prev.next.next
        
        # now prev is the head with the node cutted

        return self.reverse_node(reverse)


        

     

    def reverse_node(self,head):
        reverse = None
        curr = head 

        while curr:
            temp = curr.next
            curr.next = reverse

            reverse = curr # pointer of reverse 
            curr = temp    # Pointer of current
        
        return reverse
    def print_node(self,head):

        while head:
            print(head.val)
            head = head.next