""" Author : Alagusundaram Nithyanandam | LeetCode Solution : Number of Substrings Containing All Three Characters
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
"""

s = "aabcabc"
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans, lo, cnt = 0, -1, {c : 0 for c in 'abc'}
        for hi,c in enumerate(s):
            cnt[c]+=1
            print(cnt)
            while all(cnt.values()):
                ans+=len(s)-hi
                lo+=1
                print (lo)
                cnt[s[lo]]-=1
        return ans
##        return ans


instance_of_solution=Solution()
print(instance_of_solution.numberOfSubstrings(s))