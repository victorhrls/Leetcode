"""
LeetCode - Valid Anagram
Difficulty: Easy
https://leetcode.com/problems/valid-anagram/

Problem:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


Approach:
"""


# i could just count the freq of each letter , if it is equal it works

# the alphabet has 26 caracthers 
# making any caracther - 'a' i can get to the relative value 
# because 'a' is the first ascii value , so we get the order of the alphabets



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import numpy as np
        if len(s) != len(t):
            return False
        
        count = np.zeros(26) # creates an array of 26 spaces 0

        for ch in s: #taking the caracther
            count[ord(ch) - ord('a')] +=1  #ord takes a string and see the value

        # now compare

        for ch in t:
            if count[ord(ch) - ord('a')] == 0: 
                return False #tem letras que nao tem no s
            count[ord(ch) - ord('a')] -=1

        return True

        

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

