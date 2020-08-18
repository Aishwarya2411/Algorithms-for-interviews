from functools import lru_cache

class Solution(object):
    @functools.lru_cache(None)
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        
        if n<=1:
            return n
        else:
            return 1+ min(n%2+ self.minDays(n//2), n%3+self.minDays(n//3))
        
