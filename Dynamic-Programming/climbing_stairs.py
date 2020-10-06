""" Leet Code Solutions #70 : Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Solution Algorithm : Dynamic Programming
"""

n=5

class Solution:
    def climbStairs(self, n: int) -> int:

        dict={1:1,2:2}

        if n ==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(3,n+1):
            dict[i]=(dict[i-1]+dict[i-2])

        return dict[n]

ins=Solution()
print(ins.climbStairs(n))