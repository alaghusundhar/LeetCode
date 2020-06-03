""" Author : Alagusundaram Nithyanandam | Leet Code Solution : Maximum Product of Two Elements in an Array
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
Example 1:
Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""
nums = [3, 4, 5, 2]
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = nums[0]
        second_max = 0
        for i in range(1, len(nums)):
            if nums[i] >= max_value:
                second_max = max_value
                max_value = nums[i]
            elif nums[i] > second_max:
                second_max = nums[i]
        return (max_value - 1) * (second_max - 1)


instance_of_Solution = Solution()
print(instance_of_Solution.maxProduct(nums))
