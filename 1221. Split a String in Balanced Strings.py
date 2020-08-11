class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        var=0 
        ans=0
        for char in s:
            if char == 'L':
                var+=1
            else:
                var-=1
            if var==0:
                ans+=1
        return(ans)
