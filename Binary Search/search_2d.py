"""
LeetCode  - Search a 2D Matrix
Difficulty: Medium
https://leetcode.com/problems/search-a-2d-matrix/description/

Problem:
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Approach:
"""



# This is still not O(log(m*n)) but until now it suits well
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


#string = [[1,2,3,6,8,10,12],[10,12]]
#goal = 10
#size = len(string)
#print(len(string[0]))


def searchMatrix(matrix,target):
    for element in range(len(matrix)):
        start = 0
        ending = len(matrix[element]) -1
        search = binary_search(matrix[element],target,start,ending)    

        if search:
            return True
    return False


#print(string[1])

#print(binary_search(string[1],goal,0,len(string[1]) -1))