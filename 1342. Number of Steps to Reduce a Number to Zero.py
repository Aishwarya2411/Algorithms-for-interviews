class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        
        n=0
        while num!=0:
            if num%2==0:
                num=num/2
                n+=1
            else:
                num-=1
                n+=1
        return n
                
            
        
