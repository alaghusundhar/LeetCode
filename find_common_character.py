""" Leet Code Solution:
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Input: ["bella","label","roller"]
Output: ["e","l","l"]
"""


from typing import List
import sys

from urllib3.connectionpool import xrange

abcd=["bella","label","roller"]


class Solution:

    def commonChars(self, A: List[str]) -> List[str]:

        answer=None
        for a in A:
            work = {}
            for b in a:
                if b in work:
                    work[b]+=1
                else:
                    work[b]=1
            if answer !=None:
                keys=list(answer.keys())
                for k in keys:
                    if k in work:
                        answer[k] = min(answer[k], work[k])
                    else:
                        del answer[k]
            else:
                answer=work
        answerArr = []

        for key in answer:
            count = answer[key]
            for _ in xrange(count):
                answerArr.append(key)

        return answerArr

ins=Solution()
print(ins.commonChars(abcd))
