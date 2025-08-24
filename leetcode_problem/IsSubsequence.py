class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        memiry = []
        for i in range(0,len(t)):
            if t[i] in s:
                memiry.append(t[i])
        if len(memiry) < len(s):
            return False
        for i in range(0,len(s)):
            if s[i] not in memiry:
                return False
            if s[i] == s[len(s)-1]:
                return True
            if memiry.index(s[i]) > memiry.index(s[i+1]):
                return False
        return True