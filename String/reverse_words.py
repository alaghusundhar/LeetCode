

s="Let's take LeetCode contest"
words = s.split()
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in words)

ins=Solution()
print(ins.reverseWords(s))