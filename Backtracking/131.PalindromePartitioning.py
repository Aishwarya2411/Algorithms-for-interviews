class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs (s, pal, res):
            if not s:
                res.append (pal)
                return 
            for i in range (1, len(s)+1):
                if palindrome (s[:i]):
                    dfs(s[i:], pal+[s[:i]], res)
        
        def palindrome (s):
            return s==s[::-1]
        
    
        
        res=[]
        dfs(s, [],res)
        return (res)
