"""
LeetCode - Valid Sudoku
Difficulty: Medium
https://leetcode.com/problems/valid-sudoku/description/

Problem:

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.


Approach:

# try using set later
"""
import numpy as np


#novo_dicionario = {int(x) : 0 for x in np.arange(1,10)}

#print(novo_dicionario)

# So it is a 9x9 board
# Each row got to have 1-9 numbers ( no repetition )
# Each column got to have 1-9 numbers (no repetition)

# Each sub matrix (3x3) must have (1-9) without repetition

# ONLY the filled cells nees to be validated


ex1 =[["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]


ex2 =[["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]


ex3 = [
    ['8', '3', '.'],
    ['6', '.', '.'],
    ['.', '9', '8']
]

# There are 9 blocks 3x3 to verify




def valid_sudoku_block(matrix,size = 3):
    # To verify each rule i should work with SETS
    # row r , column c -> Run through (r,c)
    # When it will be a subset?  -> Row = 0,3,6 / Column = 0,3,6
    # First attempt -> Just one set of 9x9 and verify
    # What we have to VERIFY

    rule = {str(x):0 for x in np.arange(1,10)}
    
    for row in range(size):
        for col in range(size):

            element = matrix[row][col]
            # Is it empty ?

            if element != '.': 
                if rule[element] ==1 : # already was there
                    return False
                else:
                    rule[element] +=1
    return True
            

def valid_row(matrix_row,size = 9):

    # the row is fixed
    row_rules = { str(i) : 0 for i in np.arange(1,10)}
    for col in range(size): # so iterate EACH col and see what happens
        element = matrix_row[matrix_row][col]

        if element != '.':
            if row_rules[element] == 1: return False
            else: row_rules[element] +=1
    return True

def valid_col(matrix_col,size = 9):

    col_rules = {str(i):0 for i in np.arange(1,10)}
    for row in range(size):
        element = matrix_col[row][matrix_col]

        if element != '.':
            if col_rules[element] == 1 : return False
            else : col_rules[element] +=1

    return True


    

def is_valid_sudoku(matrix):


    size = len(matrix)

    for element in range(size): 

        # Check line and column

        col_ele = valid_col
        row_ele = valid_row

        # Then if the element is in some square ,check the 3rd condition
        if element %3 == 0 : # so it is a new block
            block_ele = valid_sudoku_block

        if not col_ele or not row_ele or not block_ele : return False


    
