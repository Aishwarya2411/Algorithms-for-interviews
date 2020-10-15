class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
       
        def dfs(i, j, balance, combination):
            
          
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or balance==len(word) or board[i][j]!= word[balance] or board[i][j]=="#":
                if balance==len(word):
                        return True
                            
            
                return False 
            
            combination+=board[i][j]
            temp= board[i][j]
            board[i][j]="#"
            balance+=1
            
            
            for row, col in [(0,1),(1,0), (0,-1), (-1,0)]:
                if dfs(i+row, j+col, balance, combination):
                    return True
                    
            board[i][j]= temp
            return False
        combination=""   
        for i in range (len(board)):
            for j in range (len(board[0])):
                
                    
                   if dfs (i,j,0,combination):
                   
                      return True
        return False
       
            
     
