class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        """"Take 2 conditions, the next entry can be either 0 or between 1-9,
        if 0:
            see if the last element is non zero and together with the last element the number is between 1 to 26:
             if yes, the dp entry will be same as the entry of dp[i-2]
        if non-zero:
            dp[i]= dp[i-1]
            and see  if the last element is non zero and together with the last element the number is between 1 to 26: 
            if yes, 
             dp[i]+= dp[i-2]
        """
        if s==" ":
            return 0
    
        dp=[0]*len(s)
        if int(s[0])==0:
            return 0
        if 1<=int(s[0])<=26:
            dp[0]=1
        for i in range (1, len(dp)):
            
            if 1<=int(s[i])<=9:
                dp[i]= dp[i-1]
                if int(s[i-1])!=0:
                    if i==1 and 1<=int(s[i-1]+s[i])<=26:
                        dp[i]+=dp[i-1]
                    if i!=1 and 1<=int(s[i-1]+s[i])<=26:
                        dp[i]+=dp[i-2]
            elif int(s[i])==0:
                if i>1:
                    if int(s[i-1])!=0 and 1<=int(s[i-1]+s[i])<=26:
                        dp[i]= dp[i-2]
                if i==1 and int(s[i-1])!=0 and 1<=int(s[i-1]+s[i])<=26:
                        dp[i]= dp[i-1]
                        
        return (dp[-1])
                
                
            
