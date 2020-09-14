"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
"""

from typing import List
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        count={}
        combined_array=arr1+arr2+arr3
        for i in combined_array:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        return sorted([key for key,value in count.items() if value==3])



ins=Solution()
print(ins.arraysIntersection(arr1,arr2,arr3))