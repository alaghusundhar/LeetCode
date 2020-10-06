""" Leet Code Solution # 1099 - Two Sum Less Than K

Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.

Algorithm Used : Two Pointers

Time and Space Complexity : TBD
"""



from typing import List

A = [34,23,1,24,75,33,54,8]
K = 60

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:

        a=sorted(A)
        start=0
        end=len(sorted(A))-1
        ans=-1
        while start < end:
            if a[start] + a[end] < K:
                ans=max(ans,a[start] + a[end])
                start+=1
            else:
                end-=1
        return ans


ins=Solution()
print(ins.twoSumLessThanK(A,K))