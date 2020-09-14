from typing import List

s=["h","e","l","l","o"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print (s)


ins=Solution()
ins.reverseString(s)