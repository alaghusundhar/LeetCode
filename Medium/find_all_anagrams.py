""" Author : Alagusundaram Nithyanandam | Leetcode Solution - Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""


from collections import Counter
from typing import List

s="cbaebabacd"
p= "abc"
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pCounter=Counter(p)
        sCounter=Counter(s[:len(p)-1])

        for c in range(len(p)-1,len(s)):
            sCounter[s[c]]+=1
            if sCounter==pCounter:
                res.append(c-len(p)+1)
            sCounter[s[c - len(p) + 1]] -= 1
            if sCounter[s[c - len(p) + 1]] == 0:
                del sCounter[s[c - len(p) + 1]]
        return res

instance_os_solution=Solution()
print(instance_os_solution.findAnagrams(s,p))
