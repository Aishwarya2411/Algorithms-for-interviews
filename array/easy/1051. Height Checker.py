class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights =sorted(heights) 
        output=0
        if heights==sorted_heights:
            return 0
        else:
            for i in range (len(heights)):
                if heights[i]!=sorted_heights[i]:
                    output+=1
        return (output)
            
