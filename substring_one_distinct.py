"""
Given a string S, return the number of substrings that have only one distinct letter.

Example :

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
"""

S="aaaba"

class Solution:
    def countLetters(self, S: str) -> int:
        count=0
        total=0
        previous=0
        for i in range(len(S)):
            if S[i]==S[previous]:
                count+=1
                previous=i
                print(S[i],S[previous])
            else:
                print(S[i], S[previous],"else")
                count=1
                previous=i

            total+=count
        print(total)
        return total
ins=Solution()
ins.countLetters(S)

