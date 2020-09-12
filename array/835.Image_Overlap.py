class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        def overlap(imgA,imgB):
            n= len(imgA)
            count=0
            for x in range (n):
                for y in range (n):
                    temp=0 
                    for i in range (y,n):
                        for j in range (x,n):
                             if imgA[i][j]==1 and imgB[i-y][j-x]==1:
                                    temp+=1
                    count= max(count, temp)
            return (count)
        temp1=overlap(A,B)
       
        temp2= overlap(B,A)
      
        return max(temp1, temp2)
        
