class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i in range (len(nums)):
            sub= target-nums[i]
            index=i
            if sub in hashmap and hashmap[sub]!=index:
                 
                return [hashmap[sub], index]
            hashmap[nums[i]]=index
        
  
