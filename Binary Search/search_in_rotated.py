"""
LeetCode  - Search in Rotated Sorted Array
Difficulty: Medium
https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Approach:
"""


nums = [4,5,6,7,0,1,2]
target = 0
#nums = [4,5,6,7,0,1,2], target = 3

# Since it has to be O(log n) and we have to find
# a target on this ORDERED list -> Binary Search


def search_rotated(nums,target):
    
    left = 0
    
    right = len(nums)-1       

    while left <= right:
        mid = (left + right)//2
        
        if nums[mid] == target:
            return mid
        

        if nums[left] < nums[mid]:  # left side is sorted
            if nums[left]  <= target< nums[mid]:
                right = mid -1
            else:
                left = mid+1
        else:                       # right side is sorted
            if nums[mid]  <target <= nums[right]:
                left = mid +1
            else: 
                right = mid -1
            
        
    return -1
                
            

print(search_rotated(nums,target))