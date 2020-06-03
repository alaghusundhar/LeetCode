"""
The ASCII codes for A-Z is 65-90 and those for a-z is that range plus 32.

Edit: Stop using range(65,91) to avoid creating these on every iteration.
"""

str = "HeLLO"


class Solution:
    def toLowerCase(self, str: str) -> str:
        abc = ""
        for i in str:
            if ord(i) >= 65 and ord(i) <= 90:
                abc += chr(ord(i) + 32)
            else:
                abc += i
        return abc

    def toLowerCaseOneliner(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if "A" <= c <= "X" else c for c in str)


instance_of_solution = Solution()
print(instance_of_solution.toLowerCase(str))
print(instance_of_solution.toLowerCaseOneliner(str))
