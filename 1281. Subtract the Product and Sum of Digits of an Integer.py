class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        add =0
        while n>0:
            digit=n%10
            product*=digit
            add+=digit
            n=n/10
        return (product-add)
