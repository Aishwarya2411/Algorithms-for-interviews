class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def permutation (first):
            if first==len(nums):
                res.append(nums[:])
            for i in range (first, len(nums)):
                temp= nums[first]
                nums[first]= nums[i]
                nums[i]= temp
                permutation(first+1)
                temp= nums[first]
                nums[first]= nums[i]
                nums[i]= temp
        permutation(0)
       
        return res
                
        
