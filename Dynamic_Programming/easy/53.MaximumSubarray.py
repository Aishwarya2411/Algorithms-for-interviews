class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        min_sum=nums[0]
        res=nums[0]
        
        for i in range (1, len(nums)):
            prev_max=max_sum
            max_sum= max(max_sum+nums[i], nums[i], min_sum+nums[i])
            min_sum= min(prev_max+nums[i], nums[i], min_sum+nums[i])
            res= max(res, max_sum)
        return res
