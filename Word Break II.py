class Solution(object):
   
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp={}
        
        
        def word(s):
          
            if s in dp:
                
                return dp[s]
            res=[]
            for w in wordDict:
                if s.startswith(w):
                    if len(s)==len(w):
                        res.append(s)
                    else:
                        strings=word(s[len(w):])
                        for string in strings:
                            res.append(w+ " "+ string)
            dp[s]=res
           
            return res
            
       
        return word(s)
                    
