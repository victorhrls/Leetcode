"""
LeetCode  - Min Stack
Difficulty: Medium
https://leetcode.com/problems/min-stack/description/


Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Approach:
Stack
"""


class MinStack:

    def __init__(self):
        self.stack =[]
        # minimum

        self.min = []

    def push(self, val):
        self.stack.append(val)

        if not self.min or val <= self.min[-1]:
            self.min.append(val)


    def pop(self):
        if self.stack: 
            val = self.stack.pop()
            if val == self.min[-1]: # i will remove from min if it is the same
                self.min.pop()
            return val
        return None

    def top(self):
        if self.stack: return self.stack[-1]
        return None 

    def getMin(self): 
        # how to remember the minimum value without seeing all the list
        if self.min:
            return self.min[-1]
        return None 

