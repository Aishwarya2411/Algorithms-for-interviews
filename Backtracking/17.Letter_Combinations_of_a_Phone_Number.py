class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}    
        
        
        
        res=[]
        def combination (curr,remain_digits):
            if not remain_digits:
                res.append(curr)
                return
           
            for letter in (phone[remain_digits[0]]):
               
                combination(curr+letter,remain_digits[1:])
                
               
                
        if len(digits)==0:
            return res 
        combination ("", digits)
       
        return res
