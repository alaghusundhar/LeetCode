# Author: Alagusundaram Nithyanandam
## Leet Code Solution
## Given an array of integers, return indices of the two numbers such that they add up to a specific target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## Example: Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

nums=[2,4,7,9,8]
target=9

class Solution():
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            number = target - num
            if number not in map:
                map[num] = i
            else:
                return [map[number], i]

foo=Solution()
print(foo.twoSum(nums,target))