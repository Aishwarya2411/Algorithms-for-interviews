class Solution(object):
    def singleNumber(self, nums):
        """u
        :type nums: List[int]
        :rtype: int
        """
        element=[]
        for i in nums:
            if (nums.count(i)==1):
                return (i)
            
