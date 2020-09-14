"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

from typing import List

n=3
class Solution:
    def sumZero(self, n: int) -> List[int]:
        L= n // 2
        reminder= n % 2
        if reminder !=0:
            answer=[0]
        else:
            answer=[]
        for i in range(1,L+1):
            print(i)
            answer.append(i)
            answer.append(-i)
        return answer


ins=Solution()
print(ins.sumZero(n))