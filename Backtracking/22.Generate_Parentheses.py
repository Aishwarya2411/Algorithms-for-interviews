class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ###dfs 
        def parenthesis (result, string, left, right):
            if left==0 and right==0:
                result.append (string)
                return  
            if left> right or left<0:           ###you can add right bracket only if you have left. 
                return 
            parenthesis (result, string+ "(", left-1, right)
            parenthesis (result, string+ ")", left, right-1)
        result =[]
        parenthesis (result, "", n,n)
        return result 
