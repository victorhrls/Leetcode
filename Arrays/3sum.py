"""
LeetCode  - 3Sum
Difficulty: Medium
https://leetcode.com/problems/3sum/description/

Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Approach:
"""

nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    size = len(nums)
    result = True 

    while result:
        for i in range(size):
            sub_array = nums[i+1:size-2]
            init = -nums[i]
            double_sum = twoSum(sub_array,init)

            if double_sum:
                row,col = double_sum 
                result = False
    return [nums[i],nums[row],nums[col]]

def twoSum(nums,target = 0):
    size = len(nums)
    for i in range(size):
        result = nums[i]            # testing for the first number
        for j in range(i+1,size):
            result += nums[j]
            if result == target:
                return i,j
            result = nums[i]
        return False


a,b,c = threeSum(nums)

print(a,b,c)


#row,col = twoSum(nums,)

#print(row,col)
#print(row,column)
#threeSum(nums)

