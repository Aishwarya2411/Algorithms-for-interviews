class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
            
        count=0
        for i in range (0, len(t)):
            if t[i]==s[count]:
                count+=1
            if count>=len(s):
                return True
        return False
