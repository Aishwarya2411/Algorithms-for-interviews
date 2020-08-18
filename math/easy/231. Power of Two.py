class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n>0:
            return ((math.log2(n).is_integer()))
        else:
            return False
            
        
          
