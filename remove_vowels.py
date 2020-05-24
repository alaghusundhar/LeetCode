""" Author : Alagusundaram Nithyanandam | Leet Code Solution
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
"""


class Solution:
    def removeVowels(self, S: str) -> str:
        return "".join(c for c in S if c not in "aeiou")


instance_of_solution = Solution()

print(instance_of_solution.removeVowels("ahdveidgoubmnnj"))
