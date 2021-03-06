""" Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (i.e.,
buy one and sell one share of the stock), design an algorithm to find the maximum profit.Note that you cannot sell a stock before you buy one.
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
              Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
prices = [7, 1, 5, 3, 6, 4]

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = profit = 0
        for price in reversed(prices):
            highest = price if price > highest else highest
            current = highest - price
            profit = current if current > profit else profit

        return profit


instace_of_solution = Solution()

print(instace_of_solution.maxProfit(prices))
