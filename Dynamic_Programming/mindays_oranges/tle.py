from functools import lru_cache

class Solution(object):
    @functools.lru_cache(None)
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        
        dp=[0]+[n+10]*n
        ##tried like coin change problem##
        
        for i in range (1,len(dp)):
            c=[1]
            if i%2==0:
                c.append(i//2)
            if i%3==0:
                c.append(2*i//3)
            for entry in c:
                
                dp[i]= min(dp[i-entry]+1, dp[i])
            
        if dp[-1]==n+10:
            return (-1)
        else:
            return(dp[-1])
