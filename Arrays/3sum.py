"""
LeetCode  - 3Sum
Difficulty: Medium
https://leetcode.com/problems/3sum/description/

Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Approach:
sort
"""

class Solution:
    def threeSum(self, nums):
        triplets =[]
        size = len(nums)
        nums.sort()         #easier to work because i can see the extremes

        for i in range(size-2):
                            #i lock the first number
            j = i+1         # next number
            k = size -1
            if i >0 and nums[i] == nums[i-1]:
                continue # skip everything , not having doubles etc
            while j<k:
                first = nums[i]
                second = nums[j]
                last = nums[k] # last number

                total = first+second+last 

                if total > 0:
                    k=k-1
                elif total <0:
                    j = j+1
                else:
                    triplets.append([first,second,last])
                    j = j +1 

                    if j<k and nums[i] == nums[j]:
                        j = j+1
        
        return triplets





        