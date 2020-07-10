"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

"""
nums = [2,5,1,3,4,7]

from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mylist=[]
        for indx,num in zip(nums[0:n],nums[n:]):
            mylist+=[indx,num]
        print(mylist)




ins=Solution()
ins.shuffle(nums,3)

