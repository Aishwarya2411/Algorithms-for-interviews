class Solution:
    def findPermutation(self, s: str) -> List[int]:
         
         
         """Keep adding values (1 to n) to a stack until char "I" is reached. Once "I" is reached empty the stack """
         
         stack=[]
         res=[]
         for i in range (len(s)):
                
                stack.append(i+1)
                
                if s[i]=='I':
                    while stack:
                       
                        res.append(stack.pop())
         
         res.append(len(s)+1)     """appending the last element"""
         while stack:             """If the last entry on the s is "D", empting the stack here will sort the last 2 elements"""
                
                res.append(stack.pop())
                
                
                
         return (res)
