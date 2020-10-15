class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        for i in range (len(mat)):
            for j in range (len(mat[0])):
                if mat[i][j]==1:
                    col= [mat[row][j] for row in range(len(mat))]
                    Row= [mat[i][column] for column in range(len(mat[0]))]
                    if col.count(1)==1 and Row.count(1)==1:
                        count+=1
        return (count)
                    
