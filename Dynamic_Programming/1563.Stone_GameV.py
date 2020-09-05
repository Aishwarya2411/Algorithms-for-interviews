class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        
        """First approch: 77/131 test cases passed,this approach does not consider all possibilities, approch-- dp list - sum of current+ prev value. do curr= curr+ prev in reverse manner and consider the min value as curr, when the while loop breaks, split as left and right list
        def stone(stoneValue, alice):


            if len(stoneValue)==1:
                return alice
            
            dp=[0]*len(stoneValue)

            for i in range (0,len(dp)):
                dp[i]= dp[i-1]+stoneValue[i]

            k = len(dp)-1
            
            if dp[k]> stoneValue[k]:
                        dp[k]= stoneValue[k]
            k= len(dp)-2

            while k>0 and dp[k]>dp[k+1]+stoneValue[k]:
                    dp[k]=dp[k+1]+stoneValue[k]
                    k-=1
            left=stoneValue[:k+1]
            right=stoneValue[k+1:]
           
            
            alice+=min(sum(left), sum(right))
            if sum(left)<sum(right):

                    score=stone(left,alice)
            elif sum(left)==sum(right):
                
                    score=max(stone(left,alice),stone(right,alice))
  
            else:
                    score=stone(right,alice)
        
            if score:
                   return score


        score=stone(stoneValue,0)
        return(score)"""
        
        """Second approach: using dp and dfs-- getting TLE"""
        
        
        
        
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
          @functools.lru_cache(None)
          def dfs(i,j):
                
                if i==j:
                    return 0
                result=0
                for k in range (i,j):
                    
                    left=dp[k+1]- dp[i]
                    right= dp[j+1]- dp[k+1]
                    
                    if left<=right:
                        result= max(result, dfs(i, k)+ left)
                        
                    if left>=right:
                        result= max(result, dfs(k+1,j)+ right)
                return result 
            
        

            
            
          dp=[0]*(len(stoneValue)+1)

          for i in range (len(stoneValue)):
                
                dp[i+1]= dp[i]+stoneValue[i]
                
          return (dfs(0, len(stoneValue)-1))
          
            
