class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs (node):
            x,y=(node)
          
            if [x,y]==destination:
                return True

            dirs=[(0,1), (0,-1), (1,0), (-1,0)]
            for d in dirs:
                dx, dy=d[0], d[1]
                a,b=x,y
"""The ball keeps movinf in one direction until it hits the wall"""
                while 0<=a+dx<len(maze) and 0<=b+dy<len(maze[0]) and maze[a+dx][b+dy]==0:
                    a+=dx
                    b+=dy
                   
                if (a,b) not in visited:
                    visited.add((a,b))
                    if dfs((a,b)):
                        return True
            
            return False  
        
                    
        visited= set()
        
             
        for i in range (len(maze)):
            for j in range (len(maze[0])):
                if i== start[0] and j==start[1]:
                    visited.add((i,j))


                    node=(i,j)
                    if dfs(node):
                        return True

        return False
