class Solution:
    def maxProduct(self, nums: List[int]) -> int:
          max_product= nums[0]
          min_product= nums[0]
          result= nums[0]
          for i in range (1,len(nums)):
             prev_max= max_product
             max_product= max(max_product*nums[i], nums[i], min_product*nums[i])
             min_product= min(prev_max*nums[i], nums[i], min_product*nums[i])
             result= max(result, max_product)
          return (result)
