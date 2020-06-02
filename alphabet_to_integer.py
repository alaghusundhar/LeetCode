""" Author : Alagusundaram Nithyanandam | Leet Code Solution - Decrypt String from Alphabet to Integer Mapping
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
eg Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
"""

s="911#12"
class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s

instace_of_solution = Solution()
print(instace_of_solution.freqAlphabets(s))