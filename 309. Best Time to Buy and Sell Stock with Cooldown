class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        options=3
        if len(prices)<1:
            return 0
        else:
            A,B,C= int(), -prices[0], int()
            for price in prices:

                    prev_A=A
                    prev_C=C
                    C= B+ price
                    prev_B=B
                    B= max(prev_A-price, prev_B)
                    A=max(A,prev_C)

            return (max(A,B,C))
