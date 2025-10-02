"""
LeetCode - Valid Anagram
Difficulty: Easy
https://leetcode.com/problems/valid-anagram/

Problem:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


Approach:
"""


# two strings
# if it is anagram ,return true 
# s and t are lowercase 

''' 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)

        if size_s != size_t:
            return False
        else:
            new_s = ''.join(sorted(s))
            new_t = ''.join(sorted(t))

            for ch in range(size_s):
                if new_s[ch] != new_t[ch]:
                    return False
            return True
'''