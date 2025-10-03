"""
LeetCode - Contains Duplicate
Difficulty: Easy
https://leetcode.com/problems/contains-duplicate/description/

Problem:
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Approach:
sorting -> N Log N 
"""




'''
O(N^2) -> Time Limit
class Solution():
    def countain_duplicates(self,nums):
        for i in range (len(nums) -1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False 

'''

class Solution():
    def containsDuplicate(self,nums):
        nums.sort() # O(n log n)
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return True
        return False
        