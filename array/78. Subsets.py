class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans =[[]]
        
        for num in nums:
            
            ans += [i+[num] for i in ans]
        return (ans)
