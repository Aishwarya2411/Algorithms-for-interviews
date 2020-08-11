class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[0]+[amount+10]* amount
        for i in range (1,len(dp)):
            for c in coins:
             
                if c<=i:
                    dp[i]= min(dp[i-c]+1, dp[i])
                
                
       
        if dp[-1]==amount+10:
            return (-1)
        else:
            return (dp[-1])
