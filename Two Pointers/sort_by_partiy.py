""" Leet Code Solution # 105 - Sort Array By Parity

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Algorithm Used : Two Pointers

Time and Space Complexity : TBD

"""
from typing import List

A=[3,1,2,4]
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        start=0
        end=len(A)-1
        while start < end:
            if A[start] % 2 == 0:
                start+=1
            else:
                A[start],A[end]=A[end],A[start]
                end-=1
        return A

ins=Solution()
print(ins.sortArrayByParity(A))

