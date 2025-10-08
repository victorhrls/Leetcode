"""
LeetCode  - Binary Search
Difficulty: Easy
https://leetcode.com/problems/binary-search/description/

Problem:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Approach:
"""

class Solution:
    def search(self,seq,obj):
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
            

# Test later the recursive way


'''

def binary_search(seq,goal,start,end):
    # start = 0
    # end = len(seq) -1

    midterm = start + (end - start)//2

    if start <= end:
        mid = seq[midterm]

        if mid == goal:
            return midterm
        elif goal > mid:
            new_start = midterm +1
            return binary_search(seq,goal,new_start,end)
        else:  #goal < mid
            new_end = midterm -1
            return binary_search(seq,goal,start,new_end)

    
    return False

'''