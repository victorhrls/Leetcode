"""
LeetCode  - Best Time to Buy and Sell Stock
Difficulty: Easy
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Approach:
"""


#no profit -> return 0
# each price[i] is the price of the stock
# on day i 

# max profit = max difference (first and last)

# profit = sell - buy >0

# if i buy on the first day, and all the following
# values are lower , i have no profit


class Solution:
    def maxProfit(self, prices):
        size = len(prices)

        profit = 0
        best = 0
        for i in range(size):
            buy = prices[i]
        
            for j in range(i+1,size):
                sell = prices[j]
                profit = sell - buy

                if (buy>sell):
                    continue
                else:
                    if profit > best: best = profit
        
        return best

        
