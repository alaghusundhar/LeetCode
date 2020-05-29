""" Author : Alagusundaram Nithyanandam | Leet Code Solution - Subtract the Product and Sum of Digits of an Integer
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
"""

import numpy as np

input =234

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0
        while n!=0:
            product = product * (n % 10)
            n = n // 10
        for i in str(input):
            sum+=int(i)
        result=product-sum
        return result

    def subtractProductAndSumOneLiner(self, n: int) -> int:
        a = [int(x) for x in str(n)]
        return np.prod(a) - np.sum(a)

instace_of_solution = Solution()

#print(instace_of_solution.subtractProductAndSum(input))
print(instace_of_solution.subtractProductAndSumOneLiner(input))