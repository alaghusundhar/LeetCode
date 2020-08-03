"""Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs."""

from typing import List

nums = [1, 2, 3, 1, 1, 3]
class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        j=0
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]== nums[j]:
                    count=count+1
        return count

ins=Solution()
ins.numIdenticalPairs(nums)