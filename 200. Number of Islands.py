class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        output=0
       
    
        for i in range (len (grid)):
            for j in range (len(grid[0])):
                
                if grid[i][j]=='1':
                    output+=self.dfs(i, j, grid)
        return (output)
    def dfs (self, i, j, grid):
            
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] =='0':
                
                return 0
                
            grid[i][j]='0'
            self.dfs(i, j-1, grid)
            self.dfs(i, j+1, grid)
            self.dfs(i+1, j, grid)
            self.dfs(i-1,j, grid)
            
            return 1
