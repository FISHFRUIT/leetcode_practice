class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1, -1 , -1):
            if s[i] == ' ':
                continue
            else:
                sum += 1
            if s[i-1] == ' ':
                return sum
        return sum
        