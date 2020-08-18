class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        edge=0
        inner=0
        
        for i in range (0, len(grid)):
            for j in range (0,len(grid[0])):
                if grid[i][j]==1:
                    edge+=1
                    if i>0 and grid[i-1][j]==1:
                        inner+=1
                    if j>0 and grid[i][j-1]==1:
                        inner+=1
       
        return (edge*4-inner*2)
