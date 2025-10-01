"""
LeetCode #1 - Two Sum
Difficulty: Easy
https://leetcode.com/problems/two-sum/

Problem:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Approach:
"""


# O(n^2) 
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):              #fix
            row = nums[i]
            rest = len(nums) -i-1
            for j in range(rest):       #run through
                column = i+j+1
                sum = row + nums[column]
                if sum == target:
                    return i,column
                else:
                    sum = 0