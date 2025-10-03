"""
LeetCode  - Valid Palindrome
Difficulty: Medium
https://leetcode.com/problems/valid-palindrome/description/

Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Approach:

"""

# convert all uppercase to lowercase
# removing non alphanumeric characters  (non letters + numbers)
# it is the same forward and backward 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ''
        for ch in s:
            if ch.isalnum():
                pal += ch.lower()

        inverse = pal[::-1]

        for i in range(len(pal)):
            if pal[i] == inverse[i]:
                continue
            else:
                return False
        return True