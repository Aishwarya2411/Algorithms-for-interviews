class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if all(nums)!=0:
            return True
        if len(nums)==1:
            return True 
        if len(nums)>1 and nums[0]==0:
            return False
        reach=0
        for i in range (len(nums)):
            
            if i>reach:
                return False
            reach = max(i+nums[i], reach)
       
        if reach>=len(nums)-1:
            return True
        
