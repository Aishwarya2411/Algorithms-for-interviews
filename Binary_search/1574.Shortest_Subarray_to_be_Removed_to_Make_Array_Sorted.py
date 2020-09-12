class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
     
         left, right=0, len (arr)-1
         while left< right:
                if arr[left+1]>= arr[left]:
                    left+=1
                else:
                    break
                    
         if left==len(arr)-1:
              return 0
         while right>0 and arr[right-1]<= arr[right]:
              right-=1
         remove= min (len(arr)-left-1, right)
         
         for i in range (left+1):
            if arr[i]<= arr[right]:
                remove= min(remove, right-i-1)
            elif right< len(arr)-1:
                right+=1
            else:
                break
         return remove 
