class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length=[]
        present=[]
        long=0
        if len(s)==0:
            return (len(s))
        else:
            i=0
            while i< len(s):
                 
                
                 if s[i] not in present:
                        if present==[]:
                            index= i
                        present.append(s[i])
                        length.append(len(present))
                        i+=1
                 else:

                    
                    i=index+1
                    present=[]
            return (max(length))
