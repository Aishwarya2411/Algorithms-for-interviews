class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return (nums[0])
        return max(self.helper(nums, 0, len(nums)-1), self.helper(nums, 1, len(nums)))
        
        
    def helper (self, nums, start, end):
        money, rob, skip=0,0,0
        for i in range (start, end):
            money= max(rob+nums[i], skip)
            rob= skip
            skip= money
        return (money)

         
