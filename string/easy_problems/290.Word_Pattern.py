class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str= str.split(" ")
      
        pattern=list(pattern)
        return (map(pattern.index, pattern)==map(str.index, str))
