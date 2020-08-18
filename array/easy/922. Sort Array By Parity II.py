
import numpy as np

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        self.A = A
        even =[]
        odd=[]
        
        
        index= np.arange(len(A))
        
        index = list(index)
      
        
        for element in (A):
            if element%2==0:
                even.append(element)
            else:
                odd.append(element)
        even_i=[]
        odd_i=[]
        for i in range (len(A)):
            if i%2==0:
                even_i.append(i)
            else:
                odd_i.append(i)
    
        A[0::2], A[1::2] = even, odd          
        return (A)
            
        
        # B = [0 for x in range(len(A))]
#         for i in range (len(A)):
#             if A[i]%2==0:
#                 if i%2==0:
#                     B[i]=A[i]
#                 else:
#                     B[i+1]=A[i]
#             else:
#                 if i%2!=0:
#                     B[i]=A[i]
#                 else:
#                     B[i+1]=A[i]
#         return(B)

    
                    
