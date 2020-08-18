class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        if len (citations)==0:
            return 0
        if all(v==0 for v in citations):
            return 0
        citations.sort(reverse= True)
        ans = [1]* len (citations)
        for i in range (len (citations)):
        
            if i+1<=citations[i]:
                ans[i]= i+1
                
        return (max(ans))
