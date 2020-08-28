from collections import deque 

class Solution:
    
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

         visited={}
        
         
         
         for i in range(len(maze)):
             for j in range (len(maze[0])):
                    visited[i,j]= float('inf')
         visited[(start[0], start[1])]=0
         
         """Got TLE while using dfs. Using bfs, as it naturally gives the shortest path easily
        In python, list can be used as queue, append() and pop() can be used to add and remove the elements. But the time complexity to add and remove will be O(N) as it involves shifing of elements, whereas if you use collections.deque and insert elements by append() and popleft() the time complexity will be O(1)"""

         q= deque()
         q.append(start)
         dirs=[(-1, 0), (1, 0), (0, -1), (0, 1)]
         while(q):
                print(q)
                node= q.popleft()
                print(node)
                x,y=node
                for d in dirs:
                    count=0
                    dx, dy=d[0], d[1]
                    a,b=x,y
                    while 0<=a+dx<len(maze) and 0<=b+dy<len(maze[0]) and maze[a+dx][b+dy]==0:
                        count+=1
                        a+=dx
                        b+=dy
                    if visited[(node[0], node[1])]+ count<visited[(a, b)]:
                         visited[(a, b)]=visited[(node[0], node[1])]+ count
                         q.append((a,b))
        
                
         x,y=destination[0],destination[1]
         if visited[(x,y)]!= float('inf'):
                return visited[(x,y)]
         else:
            return(-1) 
        
###
"""Inital dfs -- TLE 
        class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
         def dfs (node, visited):
            
            
            x,y=(node)
            
          
            

            dirs=[(-1, 0), (1, 0), (0, -1), (0, 1)]
              
            
            for d in dirs:
                count=0
                dx, dy=d[0], d[1]
                a,b=x,y
                while 0<=a+dx<len(maze) and 0<=b+dy<len(maze[0]) and maze[a+dx][b+dy]==0:
                    count+=1
                    a+=dx
                    b+=dy
                    
               
               
                if visited[(node[0], node[1])]+ count<visited[(a, b)]:


                    visited[(a, b)]=visited[(node[0], node[1])]+ count

                    dfs((a,b), visited)
            return
                        
           
        
                
         
         count=0
         visited={}
         val= float('inf')
         
         
         for i in range(len(maze)):
             for j in range (len(maze[0])):
                    visited[i,j]= float('inf')
         visited[(start[0], start[1])]=0
         out= dfs(start, visited)
         
         
         x,y=destination[0],destination[1]
         if visited[(x,y)]!= float('inf'):
                return visited[(x,y)]
         else:
            return(-1)
         
         
         return (out)
             
"""
                

     
