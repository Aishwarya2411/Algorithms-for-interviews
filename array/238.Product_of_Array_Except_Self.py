class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    """ it is given in question, that you cannot use division, so 1) for each index, store the product of its left elements 2) for each index store the product of its right elements, 3) multiply left and right elements 4) optimize the space complexity""" 
        output=[1]* len(nums)
        output[0]=1
        for i in range (1,len(nums)):
            output[i]= output[i-1]*nums[i-1]
            
        
        right=1
        for i in range (len(nums)-2, -1, -1):
            right*= nums[i+1]
            output[i]=output[i]*right
            
        return(output)
           
