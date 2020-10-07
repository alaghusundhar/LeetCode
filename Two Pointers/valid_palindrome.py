""" Leet Code Solution # 680 - Valid Palindrome -II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Algorithm : Two Pointers

Time Complexity : O(n)

Space Complexity: O(n)
"""

s="abcdefgedcba"

class Solution:
    def validPalindrome(self, s: str) -> bool:

        start=0
        end=len(s)-1

        while start < end:
            if s[start] != s[end]:
                one,two=s[start:end],s[start+1:end+1]
                print (one,two)
                print(one[::-1])
                print(two[::-1])
                return one==one[::-1] or two==two[::-1]
            start,end=start+1,end-1

ins=Solution()
print(ins.validPalindrome(s))