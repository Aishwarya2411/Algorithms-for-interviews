class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        even=[]
        for num in nums:
            digits=[]
            while num>0:
                a = num%10
                num=num/10
                digits.append(a)
            if len(digits)%2==0:
                even.append(digits)
        return(len(even))
                
