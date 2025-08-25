class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        step = []
        answer = 0
        for i in range(0,len(s)):
            if s[i] in step:
                idx = step.index(s[i])
                step = step[idx+1:]
            step.append(s[i])
            answer = max(answer, len(step)) 
        return answer