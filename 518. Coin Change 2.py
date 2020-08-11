class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        denomination= [1]+[0]*amount
        for coin in coins:
            for i in range (coin, len(denomination)):
                denomination[i] +=denomination[i-coin]
                
        
        
        
        
        return (denomination[-1])
