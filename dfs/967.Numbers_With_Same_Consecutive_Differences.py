class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        output=[]
        
        
        def dfs(digit, N):
            
            if N==0:
                output.append(digit)
                return 
            last_digit=digit%10
            
            if last_digit>=K:
                dfs(digit*10+last_digit-K, N-1)
            if K>0 and 0<=last_digit+K<=9:
                dfs(digit*10+last_digit+K,N-1)
            
        
        
        
        
        if N==1:
            output.append(0)
        
        
        
        for i in range (1,10):
            dfs(i, N-1)
          
        return (output)
            
        
