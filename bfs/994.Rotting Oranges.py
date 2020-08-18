class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten=[]
        fresh=0
        time =0
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]==2:
                    rotten.append([i,j])
                if grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        while (len(rotten))>0:
            temp=fresh
           
            for i in range (len(rotten)):
                
               
                    x,y= rotten[0]
                   
                    rotten.pop(0)
                    
                    grid, fresh, rotten= self.bfs (x-1,y, grid, fresh, rotten)
                 
                   
                    grid, fresh, rotten= self.bfs (x,y-1, grid, fresh, rotten)
                   
                    
               
                    grid, fresh, rotten= self.bfs (x,y+1, grid, fresh, rotten)
                   
                    
                    grid, fresh, rotten= self.bfs (x+1,y, grid, fresh, rotten)
                   
            
            
            if len(rotten)>0:
                    
                    if fresh<temp:
                        time+=1
           
        if fresh!=0:
            return (-1)
        else:
            return (time)
    def bfs (self,x,y, grid, fresh, rotten):
            if 0<=x<len(grid) and 0<=y<len(grid[0]):
                if grid[x][y]==1:
                    grid[x][y]=2
                    rotten.append([x,y])
                    fresh-=1
                    
            return (grid, fresh, rotten)
                
                
                
