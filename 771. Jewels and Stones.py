class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for i in (J):
            temp = S.count(i)
            count+=temp
            
        return(count)
        
