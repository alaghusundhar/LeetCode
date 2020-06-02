""" Author : Alagusundaram Nithyanandam | Leet Code Solution - Split a String in Balanced Strings
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.
eg Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""

s="RLRRLLRLRL"
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total=counter=0
        for i in s:
            if(i=='L'): counter+=1
            if(i=='R'): counter-=1
            if(counter==0): total+=1
        return total


instance_of_solution=Solution()
print(instance_of_solution.balancedStringSplit(s))