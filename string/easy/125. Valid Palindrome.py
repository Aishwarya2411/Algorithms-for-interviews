class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = filter(str.isalnum, str(s.lower()))
        
        if s is " ":
            return True
        else:
            
            
           
            reverse = s[::-1]

            if s==reverse:
                return True
            else:
                return False
