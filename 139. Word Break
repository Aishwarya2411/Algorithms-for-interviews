class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[True]+[False]*len(s)
        for i in range (1,len(dp)):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i]|=dp[i-len(word)]
        return (dp[-1])
