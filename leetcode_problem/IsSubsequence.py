class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        timd = []
        for i in range(0,len(t)):
            if t[i] in s:
                timd.append(t[i])
        if len(timd) < len(s):
            return False
        for i in range(0,len(s)):
            if s[i] not in timd:
                return False
            if s[i] == s[len(s)-1]:
                return True
            if timd.index(s[i]) > timd.index(s[i+1]):
                return False
        return True