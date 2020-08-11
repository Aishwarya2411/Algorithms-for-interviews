import numpy as np
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # full=[]
        # for i in range (0, (len(nums)/2)):
        #     a,b= nums[2*i],nums[2*i+1]
        #     initial=np.repeat(b,a)
        #     full.append(initial)
        # full=[item for elem in full for item in elem]
        # return (full)
        
        
        out=[]
        for i in range(0,len(nums),2):
            out.extend([nums[i+1]]*nums[i])
        return (out)
