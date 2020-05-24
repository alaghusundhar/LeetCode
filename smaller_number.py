""" Author : Alagusundaram Nithyanandam | LeetCodeSolution - How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
"""
from typing import List

nums = [8, 1, 2, 2, 3]


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        for idx, num in enumerate(sorted(nums)):
            indices.setdefault(num, idx)
        return [indices[num] for num in nums]


instance_of_solution = Solution()
print(instance_of_solution.smallerNumbersThanCurrent(nums))
