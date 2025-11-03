"""
LeetCode  - Find Minimum in Rotated Sorted Array
Difficulty: Medium
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Problem:

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Approach:
"""

# It is sorted in ASCENDING order 
# Rotated between 1 and n times

# Rotate is -> a[0] , a[1] , ... a[n-1] -> a[n-1], a[0] , a[1] , ...
# The array nums has UNIQUE elements
# Return minimum element of the array
# O(log n)

'''

nums = [3,4,5,1,2] # rotated 3 times -> Output = 1

def findMin(nums):
    
    
    min = nums[0]
    
    for num in nums:
        if num < min:
            min = num

    return min 
# Complexity O(n)

print(findMin(nums)) # This works but it IS NOT O(log N)

'''

# To be log N ,i  do not need to run all the array , i should see just half of it -> Binary Search

# Since originally it is on ASCENDING order , i should take advantage of this
# I should see where would have a deflection


#nums = [3,4,5,1,2]
#nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]

#nums = [2,3,4,5,6,1,2]
def findMin(array):
    
    left = 0
    right = len(array) - 1
    
    
    
    
    
    while left < right: # i will run throught this
        
        mid = (left+right)//2
        
        print(f"left={left}, mid={mid}, right={right} | "
              f"array[mid]={array[mid]}, array[right]={array[right]}")
        
        
        
        if array[mid] > array[right]:
            left = mid +1 # advance the left
        else:
            right = mid
            
    return array[left]
print(findMin(nums))
        