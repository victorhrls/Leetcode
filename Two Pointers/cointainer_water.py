"""
LeetCode  - Container With Most Water
Difficulty: Medium
https://leetcode.com/problems/container-with-most-water/

Problem:

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Approach:

"""

# Line 0 has height 1 -> Pos (0,1)
# Line 1 has height 8 -> Pos (1,8)

test = [1,8,6,2,5,4,8,3,7]


# Ex -> let`s  say that i pick pos 1(height 8) and pos 8 (height 7)
# So i will have that the container will have the area (8-1) * min(8,7) because the height can't pass the min (7)

# I can make by brute force checking EVERY pair -> O(n^2) , slow
# Two pointers can make it faster

def maxArea(water):

    # Area = width x height
    # Area = (j-i) * min(height(i), height(j))

    # Idea -> start with the WIDEST possible container and try to make it TALLER moving the pointers 
    # the width decreases as the pointer moves
    # To increase the area i should increase the height

    left = 0
    right = len(water) -1
    max_area = 0

    # always move the pointer to the smaller height -> only way to get bigger area
    # stop when left and right meet
    # so it is like starting with the max possible width and making a trade with height



    while left < right:

            
        width = right-left
        height = min(water[left],water[right])

        area = width*height

        if area > max_area: max_area = area

        # Now i want to see ,which side has the SMALLER height 

        # I will move the limitating height 
        if (water[left] > water[right]):
            right = right -1
        elif(water[left] < water[right]):
            left = left + 1
        else:
            # same heights 
            left +=1 # or right -=1
    
    return max_area
    
print(maxArea(test))
