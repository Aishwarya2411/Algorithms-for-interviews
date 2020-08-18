class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def fn (x,y):
           
            if x<0 or x>=length or y<0 or y>=breadth or board[x][y]!='O':
                return
            else:
                board[x][y]='dummy'
             
                fn (x-1,y)
                fn(x+1,y)
                fn (x,y-1)
                fn(x,y+1)
                
                
    

        if board!=[]:
            length = len (board)
        
            breadth = len (board[0])
            
          
 
            for i in range (0, length):

                fn(i,0)
               
                fn(i, breadth-1)

            for j in range (0, breadth):

                fn(0,j)
                fn(length-1,j)

            ref_table ={'X':'X', 'O':'X', 'dummy':'O'}

            for i in range (length):
                for j in range (breadth):
                    board[i][j] = ref_table[board[i][j]]

        
        
        
        
