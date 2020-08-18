class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n=0
        temp=0
        while temp<num:
            temp=4**n
            
            if temp==num:
                return True 
            else:
                n+=1
                continue 
            
        return False
