from typing import List

nums = [3,2,2,3]

val = 3

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

    def solutionTwo(self,nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove()
        return len(nums)

ins=Solution()
print(ins.removeElement(nums,val))
print(ins.removeElement(nums,val))