""" Author : Alagusundaram Nithyanandam | Leet Code Solution - Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.
eg Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
"""
from typing import List

input=[12,345,2,6,7896]
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count = count + 1
        return count

    def findNumbersoneliner(self, nums: List[int]) -> int:
        return sum(len(str(n)) % 2 == 0 for n in nums)

instance_of_solution = Solution()
print(instance_of_solution.findNumbers(input))