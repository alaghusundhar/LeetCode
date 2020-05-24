""" Author : Alagusundaram Nithyanandam | Leet Code Solution
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
eg Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""
ip = "10.248.1.65"


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


instance_of_solution = Solution()
print(instance_of_solution.defangIPaddr(ip))
