"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""
from typing import List
from itertools import accumulate

nums = [1,2,3,4]
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i==0:
                nums[i]=nums[0]
            else:
                nums[i]=nums[i]+nums[i-1]
        return nums

    def runningSumOneLiner(self, nums: List[int]) -> List[int]:
        from itertools import accumulate
        return accumulate(nums)

ins=Solution()
print(ins.runningSum(nums))
print(ins.runningSumOneLiner(nums))