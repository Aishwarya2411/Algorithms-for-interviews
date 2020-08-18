class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        unique=[]*(len(nums)-1)
        for i in nums:
            if i not in unique:
                unique.append(i)
            else:
                return i
        
