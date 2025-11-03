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
    
    size = len(array)
    
    key = array[size//2] # in the middle 
    left = array[size//2 -1]
    right = array[size//2+1]
    
    print()
    
    
    print(f"We are dealing with size {size} \t key = {key} \t left = {left} \t  right = {right}")
    
    print()
    
    
    # I should compare with both sides and pick it 
    found = False
    
    
    while not found:
        

        if key > left: # should continue or found it ? 
            
            print(f"So we can say that {key} > {left}")
            print()
            if right > key:
                print(f"So we can say {right} > {key}")
                
                key = array[(size//2) + 1] # still can grow 
                
                print("The key is ",key)
            if right < key: # found the counterpoint
                print(f"So we can say {right} < {key}")
                key = right

                found = True
        else: # key < left 
            # we are already on the min key
            found = True
            
    return key

print(findMin(nums))
            
            
            

           
        
        
        