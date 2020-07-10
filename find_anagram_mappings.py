""" Author : Alagusundaram Nithyanandam | LeetCode Solution - Find Anagram Mappings
Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

We should return
[1, 4, 3, 2, 0]

"""
from typing import List

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]


class Solution:
    def anagramMappingsOneLiner(self, A: List[int], B: List[int]) -> List[int]:
        return [B.index(a) for a in A]

    def anagramMappingsMap(self, A: List[int], B: List[int]) -> List[int]:
        d = {}
        for i, n in enumerate(B):
            d[B[i]] = i
            print(d)
            print(d[B[i]])
        return [d[a] for a in A]


instance_of_Solution = Solution()
print(instance_of_Solution.anagramMappingsOneLiner(A, B))
print(instance_of_Solution.anagramMappingsMap(A, B))
