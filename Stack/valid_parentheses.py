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
    size = len(s)

    
    opening = ['{','[','(']

    dic = {'}': '{' , 
           ']': '[',
           ')': '('}
    #opening and close

    # read the string , if it is opening add to the stack
    # if it is closening check with pop

    for i in range(size):
        if stack[i] in opening:
            stack.append(s[i])

            if stack.pop() !=  dic[s[i]]: # the closing is different from its dictionary ?
                return False
        return False
    

dic = {'{': '}' , 
           '[': ']',
           '(': ')'}

print(dic['{'])