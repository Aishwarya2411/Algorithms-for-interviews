class Solution:
    def rob(self, nums: List[int]) -> int:
        money, rob, skip=0,0,0
        for i in range (len(nums)):
            money= max(rob+nums[i], skip)
            rob= skip
            skip= money
        return (money)
