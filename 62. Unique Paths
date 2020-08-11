class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp= [[0]*m for i in range(n)]
        
       
        for i in range (n):
            for j in range (m):
               
                if i==j==0:
                    dp[i][j]=1
                    if i+1<n: 
                        dp[i+1][j]=1
                    
                    if j+1<m:
                        dp[i][j+1]=1
                        
                
                elif i<=n and j<=m:
                    if dp[i][j]==0:
                        dp[i][j]=dp[i][j-1]+ dp[i-1][j]
                   
         
        return (dp[n-1][m-1])
        
