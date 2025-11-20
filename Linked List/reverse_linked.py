"""
LeetCode  - Reverse Linked List
Difficulty: Easy
https://leetcode.com/problems/reverse-linked-list/

Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Approach:
iteratively and recursively
"""

class Node:
    def __init__(self,val=0 ):
        self.val = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = Node()
        
    def append(self,value):
        new_node = Node(value)
        cur = self.head
        
        while cur.next != None: # i get to the END of the list
            cur = cur.next         
            
        cur.next = new_node
    def size(self):
        
        count = 0
        cur = self.head
        
        while cur.next != None:
            count +=1
            cur = cur.next
        
        return count
    def view(self):
        
        view = []
        cur = self.head
        
        while cur.next != None:
            cur = cur.next
            view.append(cur.val)
        
        print(view)
            
# The head is already a linked list
    
def reverse_list(head):
    direct = Linked_List()
    
    inv = head[::-1]
    for element in inv:
        direct.append(element)
        
    direct.view()
    
  
head = [1,2,3,4,5]  
reverse_list(head)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # I need 2 pointers
        curr = head 
        prev = None 
        
        
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
            