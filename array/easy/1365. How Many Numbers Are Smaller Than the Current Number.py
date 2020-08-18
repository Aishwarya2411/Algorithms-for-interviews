class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums=sorted (nums)
        index=[sorted_nums.index(i) for i in nums]
        return (index)
