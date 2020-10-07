""" Leet Code Solution # 704 - Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Algorithm : Binary Search

Time Complexity : O(log(N))
Space Complexity: TBD
"""

nums = [-1,0,3,5,9,12]
target = 9

from typing import List

class Solution:
    """ Commmon Solution - Simple Approach"""
    def search(self, nums: List[int], target: int) -> int:
        for idx,num in enumerate(nums):
            if num == target:
                return idx
        return -1

    def searchTwo(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left=mid+1
            elif nums[mid] > target:
                right=mid-1
            else:
                return mid
        return -1


ins=Solution()
#print(ins.search(nums,target))
print(ins.searchTwo(nums,target))
