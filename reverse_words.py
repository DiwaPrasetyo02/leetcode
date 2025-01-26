class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, reverse the list, and join them with a single space
        return ' '.join(s.split()[::-1])

solution = Solution()
words = "This was a good"
result = solution.reverseWords(words)
print(result)