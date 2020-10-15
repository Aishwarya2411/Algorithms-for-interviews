class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        i=2
        while i<=N:
            i*=2

        return i-1-N
       
       
