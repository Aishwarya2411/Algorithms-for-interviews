class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal1 = [mat[i][i] for i in range (len(mat))]
        n= len(mat)
        diagonal2 = [mat[i][n-i-1] for i in range (n) if i!=n-i-1]
      
        diag= diagonal1+diagonal2
        return (sum(diag))
