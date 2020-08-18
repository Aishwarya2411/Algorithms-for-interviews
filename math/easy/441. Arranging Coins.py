class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        count=1
        num_sum=0
        while num_sum<=n:
           
                num_sum+=count
                if num_sum<=n:
                    count+=1
                
        return (count-1)
                
