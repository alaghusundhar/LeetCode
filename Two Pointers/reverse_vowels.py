""" Leet Code Solution #345: Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

eg
Input: "hello"
Output: "holle"

Solution Algorithm : Two Pointers
"""

s="hello"
class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels={'a','e','i','o','u','A','E','I','O','U'}
        start=0
        end=len(s)-1
        L=list(s)
        while start < end:
            while start < end and L[start] not in vowels:
                start+=1
            while start < end and L[end] not in vowels:
                end-=1
            L[start],L[end]=L[end],L[start]
            start+=1
            end-=1
        return "".join(L)

ins=Solution()
print(ins.reverseVowels(s))