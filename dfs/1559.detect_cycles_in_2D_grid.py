class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        def dfs(grid, node, parent):
            
            (a,b)=node
           
            if node in visited:
                    return True
            visited.add(node)
            
            neighbour=[(dx,dy) for dx, dy in [[a+1,b],[a-1,b],[a,b+1], [a,b-1]]]
            neighbour=[(dx,dy) for dx, dy in neighbour if dx>=0 and dx<len(grid) and dy>=0 and dy<len(grid[0])]
           
            neighbour=[(dx,dy) for dx,dy in neighbour if grid[dx][dy]== grid[i][j] and (dx, dy)!=parent]
            
           
            for n in neighbour:
                
                if dfs(grid, n, node):
                    return True
            
            return False
                
               
                
                       
         
        visited=set()
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                
                if (i,j) in visited:
                    continue
                
                entry=(i,j)
                
                if dfs(grid, entry,None):
                    return True
        return False
       
         
