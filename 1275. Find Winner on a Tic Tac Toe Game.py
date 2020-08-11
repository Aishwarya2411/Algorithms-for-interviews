import numpy as np
class Solution(object):
    def tictactoe(self, moves):
        self.moves=moves
        result=None
        board = np.zeros ([3,3], dtype=str)
        for i in range (len(moves)):
            index = moves[i]
            a = index[0]
            b= index[1]
            if i%2==0:
                board[a][b]=str('x')
            else:
                board[a][b]=str('o')
        empty=''
        if empty not in (np.diagonal(board)):
            if (len(set(np.diagonal(board))))==1:
                if (set(np.diagonal(board)))==set(['x']):
                    result = 'A'
                else:
                    result='B'
                    
        diag2= set([board[i][len(board)-1-i] for i in xrange(len(board))])
        if empty not in diag2:
            if len(diag2)==1:
                if diag2==set(['x']):
                        result = 'A'
                else:
                    result='B'
                    
        board=board
        for i in range(len(board)):
            if empty not in board[i]: 
                if (len(set(board[i])))==1:
                    if (set(board[i]))==set(['x']):
                        result = 'A'
                    else:
                        result = 'B'
                       
            if empty not in board[:,i]: 
                if (len(set(board[:,i])))==1:
                    if (set(board[:,i]))==set(['x']):
                        result = 'A'
                    else:
                        result = 'B'
                
   
        if result == None:
            if empty not in board:
                result = 'Draw'
            else:
                result = 'Pending'
        
        return (result)
