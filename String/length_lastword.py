""" Leet Code Solutions :
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

"""
s="My Name is Alagusundar"
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split()
        length = len(split)
        if len(split) != 0:
            abcd = len(split[length - 1])
        else:
            return 0
        return abcd

ins=Solution()
ins.lengthOfLastWord(s)
