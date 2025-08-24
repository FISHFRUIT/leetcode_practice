class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        memory = []
        for i in range(0,len(t)):
            if t[i] in s:
                memory.append(t[i])
        if len(memory) < len(s):
            return False
        for i in range(0,len(s)):
            if s[i] not in memory:
                return False
            if s[i] == s[len(s)-1]:
                return True
            if memory.index(s[i]) > memory.index(s[i+1]):
                return False
        return True

    def isSubsequence2(self, s: str, t: str) -> bool:
        indexOfS = 0
        indexOfT = 0
        if len(s) == 0:
            return True 
        while indexOfT < len(t):
            if t[indexOfT] == s[indexOfS]:
                indexOfS += 1
                if indexOfS == len(s):
                    return True
            indexOfT += 1
        
        return False