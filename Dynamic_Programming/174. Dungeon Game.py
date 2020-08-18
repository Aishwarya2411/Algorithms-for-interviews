class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len (dungeon[0])
        
        if m==0 or n ==0:
            return 0
        
        
        dp =[[0 for i in range(n)] for j in range(m)]
        
        dp[m-1][n-1]=max(1, 1-dungeon[m-1][n-1])

        
        for i in reversed(range (0,m-1)):
            dp[i][n-1]= max(1, dp[i+1][n-1]- dungeon[i][n-1])
        for j in reversed (range (0,n-1)):
            dp[m-1][j]= max(1, dp[m-1][j+1]-dungeon[m-1][j])
        for i in reversed (range(m-1)):
            for j in reversed (range(n-1)):
                dp[i][j]=max(1,min(dp[i][j+1], dp[i+1][j])-dungeon[i][j])
               
        return (dp[0][0])
