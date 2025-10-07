"""
LeetCode  - Valid Parentheses
Difficulty: Easy
https://leetcode.com/problems/valid-parentheses/description/


Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Approach:
Stack
"""


s = "({[]})"



# how to use a stack on this problem

# ex 


def sol(s):
    stack = []
    
    opening = ['{','[','(']

    dic = {'}': '{' , 
           ']': '[',
           ')': '('}
    #opening and close

    for ch in s: #verify each caracther
        if ch in opening:
            stack.append(ch)
        else:
            #if it is empty
            if not stack: return False
            if stack.pop() != dic[ch]: # it is not the right one
                return False
    return len(stack) == 0 


    # read the string , if it is opening add to the stack
    # if it is closening check with pop

   
    

