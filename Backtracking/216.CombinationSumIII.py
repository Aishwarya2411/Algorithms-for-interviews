class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output=[]
        def combination (start, n, combine):
            if len(combine)==k:
                if n==0:
                    output.append(combine.copy())
                return
            
            for i in range (start, 10):
                combine.append(i)
                combination(i+1, n-i, combine)
                combine.remove(i)
        
        combination (1, n, combine=[])
        return (output)
                
        
