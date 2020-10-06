""" Leet Code Solution #1408 : String Matching in an Array

Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Algorithm : String

Time Complexity : O(N^2)

Space Complexity: O(N)

"""

from typing import List

words = ["mass","as","hero","superhero"]
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        ans=[]
        for i,word in enumerate(words):
            for j in range(i+1,len(words)):
                if word in words[j]:
                    ans.append(word)
        return ans


ins=Solution()
print(ins.stringMatching(words))
