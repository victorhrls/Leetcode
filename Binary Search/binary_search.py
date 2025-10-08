"""
LeetCode  - Binary Search
Difficulty: Easy
https://leetcode.com/problems/binary-search/description/

Problem:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Approach:
"""



def binary_search(seq,obj):
    init = 0
    ending = len(seq) - 1

    while init<=ending: # i should run all the seqs
        
        midterm = init + (ending - init)//2

        mid = seq[midterm]
        if (mid == obj):
            return midterm
        elif obj > mid:
            init = midterm + 1 #advances midterm
        else:
            ending = midterm - 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9

print(binary_search(nums,target))



