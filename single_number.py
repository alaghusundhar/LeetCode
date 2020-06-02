from typing import List
nums=[2,2,1]
class Solution():
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
            print (res)
        return res

instance_of_solution=Solution()
print(instance_of_solution.singleNumber(nums))
