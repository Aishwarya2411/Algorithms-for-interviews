class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        Count=[]
        for i in range (len(s)):
            count = s.count (s[i])
            if count ==1:
                return (i)
        
            Count.append(count)
         
        if 1 not in Count:
            return (-1)
       
            
