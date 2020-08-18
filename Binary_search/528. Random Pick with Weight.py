import random
import bisect 

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.list_sum=[0]
        for i in w:
        
            self.list_sum.append(self.list_sum[-1]+i)
       
        
    def pickIndex(self):
        
      
        
        rand = random.randint(1,self.list_sum[-1])
        
        
        output = bisect.bisect_left(self.list_sum, rand)
       
        """
        :rtype: int
        """
        return (output-1)
       


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
