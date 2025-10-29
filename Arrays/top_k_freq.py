''' 
LeetCode - Top K Frequent Elements
Difficulty: Medium
https://leetcode.com/problems/top-k-frequent-elements/

Problem:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Approach:
'''


nums = [1,1,1,2,2,3]
k = 2

#nums = [1,2,1,2,1,2,3,1,3,2], k = 2



def topKfrequent(nums,k):


    freq = {}
    for n in nums: # check the nums

        if n not in freq:
            freq[n] = 1
        else:
            freq[n] +=1


    # Now i just have to sort by value

    sorted_values = sorted(freq,key = freq.get, reverse = True)

    # Because get already verify Key -> Value !!! 

    results = sorted_values[:k] # take the k values



    return results

print(topKfrequent(nums,k))