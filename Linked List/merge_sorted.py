"""
LeetCode  - Merge Two Sorted Lists
Difficulty: Easy
https://leetcode.com/problems/merge-two-sorted-lists/

Problem:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Approach:

"""


# So , the heads are already sorted.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self,list1,list2):
        
        dummy = ListNode()
        
        curr = dummy 
        
        # pointer list 1 
        # pointer list 2
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next  # advances list1
            else:
                curr.next = list2
                list2 = list2.next  # Advances list2
                
            # Now move the dummy
            
            curr = curr.next
                
        # if 1 of the lists ends, connect
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2
                
        
        return dummy.next
        
        
        
                

def build_test(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

list1 = build_test([1,2,4])
list2 = build_test([1,3,4])

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)


def printar(node):
    while node:
        print(node.val)
        node = node.next
        
printar(merged)
